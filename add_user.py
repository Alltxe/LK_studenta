import flet as ft
from db_connection import create_connection, Error
from werkzeug.security import generate_password_hash
from datetime import datetime
from datetime import date


def openn(page: ft.Page, connection, switch=None):
    disciplines = []
    group_value = ""

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
        try:
            fields = [
                (role_field.value, "Роль не выбрана"),
                (login_field.value, "Логин не введен"),
                (password_field.value, "Пароль не введен"),
                (full_name_field.value, "ФИО не введено"),
                (date_f.value, "Дата рождения не выбрана")
            ]
            cursor = connection.cursor()
            if not all([role_field.value, login_field.value, password_field.value]):
                bottom_attention("Не все поля заполнены")
                return
            login = login_field.value
            password = generate_password_hash(password_field.value)

            if role_field.value != "Администратор":
                for value, message in fields:
                    if not value:
                        bottom_attention(message)
                        return


                birth_date = datetime.strptime(date_f.value, "%d-%m-%Y").strftime("%Y-%m-%d")
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
            else:
                cursor.execute("INSERT INTO accounts (login, password, role) VALUES (%s, %s, %s)", (login, password, "admin"))

            connection.commit()
            cursor.close()
            bottom_attention("Профиль пользователя успешно добавлен")
            clear_page()

        except Error as e:
            bottom_attention("Профиль не добавлен, проверьте поля")
            print(e)

    def on_file_selected(e):
        if file_picker.result and file_picker.result.files:
            file_path = file_picker.result.files[0].path
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Предполагаем, что файл содержит строки в формате: "ФИО, группа, дата рождения, логин, пароль"
                    students = [line.strip().split(",") for line in f.readlines()]
                    cursor = connection.cursor()

                    for student in students:
                        if len(student) >= 5:  # Проверяем, что есть минимум ФИО, группа, дата рождения, логин и пароль
                            full_name, group, birth_date, login, password = student[:5]

                            # Проверяем, существует ли указанная группа
                            cursor.execute("SELECT COUNT(*) FROM st_groups WHERE idgroups = %s", (group,))
                            if cursor.fetchone()[0] == 0:
                                bottom_attention(f"Группа '{group}' не найдена. Пропущена запись для '{full_name}'")
                                continue

                            # Добавляем запись в таблицу student
                            cursor.execute(
                                "INSERT INTO student (full_name, `group`, birth_date) VALUES (%s, %s, %s)",
                                (full_name, group, birth_date)
                            )

                            # Получаем ID добавленного студента
                            cursor.execute("SELECT LAST_INSERT_ID()")
                            student_id = cursor.fetchone()[0]

                            # Хэшируем пароль и добавляем запись в таблицу accounts
                            hashed_password = generate_password_hash(password)
                            cursor.execute(
                                "INSERT INTO accounts (login, password, role, idstudent) VALUES (%s, %s, %s, %s)",
                                (login, hashed_password, "student", student_id)
                            )

                    connection.commit()
                    cursor.close()
                    bottom_attention("Список студентов успешно загружен")
            except Exception as e:
                bottom_attention("Ошибка при загрузке списка студентов, возможно формат данных неверен")
                print(f"Ошибка: {e}")

    def clear_page():
        login_field.value = ""
        password_field.value = ""
        full_name_field.value = ""
        date_f.value = date.today().strftime("%d-%m-%Y")
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
            full_name_field.visible = True
            date_field.visible = True
            group_field.visible = False
            phone_field.visible = True

        elif role_field.value == "Студент":
            full_name_field.visible = True
            date_field.visible = True
            disciplines_section.visible = False
            group_field.visible = True
            phone_field.visible = False
            disciplines.clear()
            update_disciplines_display()

        else:
            disciplines_section.visible = False
            group_field.visible = False
            phone_field.visible = False
            full_name_field.visible = False
            date_field.visible = False

        page.update()

    def date_change(e):
        date_f.value = e.control.value.strftime("%d-%m-%Y")
        page.update()

    def group_select(e):
        nonlocal group_value
        group_value = e.selection.value


    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)

    # Поля и кнопки для добавления/удаления дисциплин
    discipline_dropdown = ft.Dropdown(
        label="Выберите дисциплину",
        icon_size=0,
    )
    add_btn = ft.ElevatedButton(text="Добавить", on_click=add_discipline)

    # Элементы формы
    role_field = ft.Dropdown(
        options=[
            ft.dropdown.Option("Студент"),
            ft.dropdown.Option("Преподаватель"),
            ft.dropdown.Option("Администратор"),
        ],
        label="Роль",
        on_change=on_role_change,
        width=431,
    )
    group_autocomplete = ft.AutoComplete(on_select=group_select)
    group_field = ft.Row(
        controls = [ft.Text("Группа", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ft.Container(content=group_autocomplete,
                               border=ft.border.all(1,ft.colors.BLACK), border_radius=ft.border_radius.all(5),
                               padding=ft.padding.only(5,0,0,5), height=50, expand=True)],
        visible=False)

    date_f = date_f = ft.TextField(hint_text='Дата',read_only=True, width=200, value=date.today().strftime("%d-%m-%Y"),
                        border=ft.InputBorder.NONE, content_padding=10, expand=True)

    date_field = ft.Row([ft.Text("Дата рождения", theme_style=ft.TextThemeStyle.BODY_LARGE),
                         ft.Container(ft.Row([
        date_f,
        ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(ft.DatePicker(on_change=date_change))
        ),
    ], width=300 ), border=ft.border.all(1, ft.colors.BLACK), border_radius=5)])

    load_list_btn = ft.ElevatedButton(text="Загрузить список", on_click=lambda e: file_picker.pick_files(allow_multiple=False))
    login_field = ft.TextField(label="Логин", max_length=45)
    password_field = ft.TextField(label="Пароль", password=True, can_reveal_password=True, max_length=45)
    phone_field = ft.TextField(label="Номер телефона", max_length=20, visible=False)
    save_btn = ft.ElevatedButton(text="Добавить", on_click=add_user)
    mode_switch_btn = ft.ElevatedButton(text="Редактирование", on_click=lambda e: switch(target="edit mode page"))

    full_name_field = ft.TextField(label="ФИО", expand=True, max_length=100)

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
            date_field,
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

