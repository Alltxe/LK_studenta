import flet as ft
from db_connection import create_connection, Error
from werkzeug.security import generate_password_hash


def open(page: ft.Page, switch=None):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.scroll = "adaptive"
    page.window.min_width = 450
    page.window.min_height = 600


    disciplines = []
    group_value = ""

    connection = create_connection()
    if connection is None:
        exit("connection timed out")


    def load_disciplines():
        """Загружает дисциплины из базы данных в Dropdown."""

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT subject_name FROM subject")  # Получаем все дисциплины из таблицы `subject`
            rows = cursor.fetchall()
            disciplines = [row[0] for row in rows]  # Извлекаем названия дисциплин

            # Обновление опций в Dropdown
            discipline_dropdown.options = [ft.dropdown.Option(discipline) for discipline in disciplines]

            page.update()

        except Error as e:
            print(f"Ошибка при загрузке дисциплин: {e}")



    def load_groups():
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT idgroups FROM st_groups")
            rows = cursor.fetchall()
            groups = [row[0] for row in rows]

            group_autocomplete.suggestions = [ft.AutoCompleteSuggestion(key=group, value=group) for group in groups]

            page.update()

        except Error as e:
            print(f"Ошибка при загрузке групп: {e}")

    def bottom_attention(text):
        snackbar.content = ft.Text(text)
        snackbar.open = True
        page.update()

    def add_user(e):
        fields = [
            (role_field.value, "Роль не выбрана"),
            (login_field.value, "Логин не введен"),
            (password_field.value, "Пароль не введен"),
            (full_name_field.value, "ФИО не введено"),
            (birth_date_field.value, "Дата рождения не выбрана")
        ]

        for value, message in fields:
            if not value:
                bottom_attention(message)
                return

        cursor = connection.cursor()
        login = login_field.value
        password = generate_password_hash(password_field.value)
        birth_date = birth_date_field.value
        role = role_field.value
        full_name = full_name_field.value
        phone_number = phone_field.value

        cursor.execute(f"SELECT COUNT(*) FROM accounts WHERE login = %s", (login,))
        if cursor.fetchone()[0] > 0:
            bottom_attention("Логин уже существует")
            cursor.close()
            return

        if role == "Преподаватель":
            query = "INSERT INTO teacher(full_name, birth_date, phone_number) VALUES (%s, %s, %s)"
            cursor.execute(query, (full_name, birth_date, phone_number))
            cursor.execute("SELECT LAST_INSERT_ID()")
            teacher_id = cursor.fetchone()[0]

            query = "INSERT INTO teacher_subjects(teacher, subject) VALUES (%s, %s)"
            for i in disciplines:
                cursor.execute(query,(teacher_id, i))
            query = "INSERT INTO accounts(login, password, role, idteacher) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (login, password, "teacher", teacher_id))

        if role == "Студент":
            # Проверяем существование group_value
            cursor.execute("SELECT COUNT(*) FROM st_groups WHERE idgroups = %s", (group_value,))
            if cursor.fetchone()[0] == 0:
                bottom_attention("Группа с таким значением не существует")
                return

            # Добавляем запись в таблицу student
            query = "INSERT INTO student (full_name, `group`, birth_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (full_name, group_value, birth_date))

            # Получаем id добавленной записи
            cursor.execute("SELECT LAST_INSERT_ID()")
            student_id = cursor.fetchone()[0]

            # Добавляем запись в accounts
            query = "INSERT INTO accounts (login, password, role, idstudent) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (login, password, "student", student_id))

        connection.commit()
        cursor.close()
        bottom_attention("Учетная запись успешно добавлена")
        clear_page()

    def clear_page():
        role_field.value = None
        login_field.value = ""
        password_field.value = ""
        full_name_field.value = ""
        birth_date_field.value = ""
        phone_field.value = ""
        discipline_dropdown.value = None
        disciplines.clear()
        page.update()

    # Контейнер для Chip элементов
    chips_container = ft.Row(
        controls=[],
        wrap=True,  # Позволяет переносить элементы на следующую строку
    )

    # Обновление отображения дисциплин
    def update_disciplines_display():
        chips_container.controls.clear()  # Очистка контейнера
        for discipline in disciplines:
            chips_container.controls.append(
                ft.Chip(
                    label=ft.Text(discipline),
                    on_delete=lambda e, d=discipline: remove_discipline(d), # Удаление дисциплины
                )
            )
        page.update()

    # Добавление новой дисциплины
    def add_discipline(e):
        selected = discipline_dropdown.value
        if selected and selected not in disciplines:
            disciplines.append(selected)
            update_disciplines_display()

    # Удаление дисциплины
    def remove_discipline(discipline):
        if discipline in disciplines:
            disciplines.remove(discipline)
            update_disciplines_display()

    # Обработка изменения роли
    def on_role_change(e):
        if role_field.value == "Преподаватель":
            disciplines_section.visible = True
            group_field.visible = False
            phone_field.visible = True
        else:
            disciplines_section.visible = False
            group_field.visible = True
            phone_field.visible = False
            disciplines.clear()
            update_disciplines_display()
        page.update()

    def data_change(e):
        birth_date_field.value = e.control.value.strftime("%Y-%m-%d")
        page.update()

    def group_select(e):
        nonlocal group_value
        group_value = e.selection.value

    # Поля и кнопки для добавления/удаления дисциплин
    discipline_dropdown = ft.Dropdown(
        label="Выберите дисциплину",
        expand=False
    )
    add_btn = ft.ElevatedButton(text="Добавить", on_click=add_discipline)

    # Элементы формы
    role_field = ft.Dropdown(
        options=[
            ft.dropdown.Option("Студент"),
            ft.dropdown.Option("Преподаватель"),
        ],
        label="Роль",
        on_change=on_role_change,  # Обработка изменения роли
    )
    group_autocomplete = ft.AutoComplete(on_select=group_select)
    group_field = ft.Row(
        controls = [ft.Text("Группа", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ft.Container(content=group_autocomplete,
                               border=ft.border.all(1,ft.colors.BLACK), border_radius=ft.border_radius.all(5),
                               padding=ft.padding.only(5,0,0,5), height=50, expand=True)],
        visible=False)

    load_list_btn = ft.ElevatedButton(text="Загрузить список")
    birth_date_field = ft.TextField(label="Дата рождения", hint_text="ГГГГ-мм-дд")
    login_field = ft.TextField(label="Логин", max_length=45)
    password_field = ft.TextField(label="Пароль", password=True, can_reveal_password=True, max_length=45)
    phone_field = ft.TextField(label="Номер телефона", hint_text="+7 ХХХ ХХХ ХХ ХХ", max_length=20, visible=False)
    save_btn = ft.ElevatedButton(text="Добавить/изменить", on_click=add_user)
    mode_switch_btn = ft.ElevatedButton(text="Редактирование", on_click=lambda e: switch(target="edit mode page"))

    full_name_field = ft.TextField(label="ФИО", expand=True)


    date_pick_btn = ft.ElevatedButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda e:
                                      page.open(ft.DatePicker(
                                        on_change=data_change
                                      )),text="выбрать дату")

    snackbar = ft.SnackBar(ft.Text(""))

    # Секция для добавления дисциплин (изначально скрыта)
    disciplines_section = ft.Column(
        controls=[
            ft.Row(
                controls=[discipline_dropdown, add_btn],
            ),
            chips_container,
        ],
        visible=False,
    )

    # Размещение элементов
    form = ft.Column(
        controls=[
            ft.Row(
                controls=[role_field,
                ft.Row(controls=[load_list_btn, mode_switch_btn])],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            group_field,
            ft.Row(controls=[birth_date_field,date_pick_btn]),
            login_field,
            password_field,
            full_name_field,
            phone_field,
            disciplines_section,
            save_btn,
            snackbar,
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=False,
    )

    # Добавление элементов на страницу
    load_disciplines()
    load_groups()
    page.add(form)

