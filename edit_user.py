import flet as ft
from db_connection import create_connection, Error
from werkzeug.security import generate_password_hash


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.scroll = "adaptive"
    page.window.min_width = 450
    page.window.min_height = 600


    disciplines = []
    group_value = ""
    students = []

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
            cursor.close()

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
            cursor.close()

        except Error as e:
            print(f"Ошибка при загрузке групп: {e}")


    def load_students_from_group(group):
        nonlocal students
        try:
            cursor = connection.cursor()
            query = "SELECT idstudent, full_name FROM student where `group` = %s"
            cursor.execute(query, (group,))
            students = cursor.fetchall()
            full_name_autocomplete.suggestions = [ft.AutoCompleteSuggestion(key=student[1], value=student[1])
                                                  for student in students]
            page.update()

        except Error as e:
            print(f"Ошибка при загрузке студентов: {e}")

    def load_teachers():
        nonlocal students
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT idteacher, full_name FROM teacher")
            teachers = cursor.fetchall()
            full_name_autocomplete.suggestions = [ft.AutoCompleteSuggestion(key=teacher[1], value=teacher[1])
                                                  for teacher in teachers]
            page.update()

        except Error as e:
            print(f"Ошибка при загрузке студентов: {e}")


    def bottom_attention(text):
        snackbar.content = ft.Text(text)
        snackbar.open = True
        page.update()

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

    navigation_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.DATE_RANGE, tooltip="Календарь"),
                ft.IconButton(icon=ft.icons.HOME, tooltip="Главная"),
                ft.IconButton(icon=ft.icons.NOTIFICATIONS, tooltip="Уведомления"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor=ft.colors.GREY_400,  # Установка цвета фона
        padding=10
    )

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

    def remove_discipline(discipline):
        if discipline in disciplines:
            disciplines.remove(discipline)
            update_disciplines_display()

    def on_role_change(e):
        if role_field.value == "Преподаватель":
            load_teachers()
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
        load_students_from_group(group_value)

    # Хранение списка студентов и текущего индекса
    students = []
    current_student_index = 0

    def full_name_select(e):
        nonlocal disciplines
        cursor = connection.cursor()
        full_name = e.selection.value
        if role_field.value == "Студент":

            query = ("""
                SELECT accounts.login, student.birth_date, student.idstudent
                FROM student
                JOIN accounts ON accounts.idstudent = student.idstudent
                WHERE student.full_name = %s
            """)
            cursor.execute(query, (full_name,))
            records = cursor.fetchall()

            if not records:
                bottom_attention("Данные не найдены")
                return

        if role_field.value == "Преподаватель":

            query = ("""
                SELECT accounts.login, teacher.birth_date, teacher.idteacher, teacher.phone_number
                FROM teacher
                JOIN accounts ON accounts.idteacher = teacher.idteacher
                WHERE teacher.full_name = %s
            """)
            cursor.execute(query, (full_name,))
            records = cursor.fetchall()

            if not records:
                bottom_attention("Данные не найдены")
                return


        current_index = 0

            # Функция для обновления данных на странице
        def update_data(index):
            nonlocal disciplines
            login_field.value, birth_date_field.value, user_id = records[index][0:3:]
            if role_field.value == "Преподаватель":
                phone_field.value = records[index][-1]
                query = ("""
                SELECT s.subject_name
                FROM teacher t
                JOIN teacher_subjects ts ON t.idteacher = ts.teacher
                JOIN subject s ON ts.subject = s.subject_name
                WHERE t.idteacher = %s
                """)
                cursor.execute(query, (user_id,))
                rows = cursor.fetchall()
                disciplines = [row[0] for row in rows]
                update_disciplines_display()


            page.update()

        # Обработчики кнопок переключения
        def prev_record(e):
            nonlocal current_index
            if current_index > 0:
                current_index -= 1
                update_data(current_index)

        def next_record(e):
            nonlocal current_index
            if current_index < len(records) - 1:
                current_index += 1
                update_data(current_index)

        # Обновление данных первой записи
        update_data(current_index)

        # Добавление кнопок навигации, если студентов с одинаковым ФИО больше одного
        if len(records) > 1:
            navigation_controls.controls = [
                ft.ElevatedButton(text="<", on_click=prev_record),
                ft.ElevatedButton(text=">", on_click=next_record),
            ]
        else:
            navigation_controls.controls = []

        page.update()

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

    birth_date_field = ft.TextField(label="Дата рождения", hint_text="ГГГГ-мм-дд")
    login_field = ft.TextField(label="Логин", max_length=45)
    password_field = ft.TextField(label="Пароль", password=True, can_reveal_password=True, max_length=45)
    phone_field = ft.TextField(label="Номер телефона", max_length=15, visible=False)
    save_btn = ft.ElevatedButton(text="Изменить")

    navigation_controls = ft.Row(
        controls=[],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    full_name_autocomplete = ft.AutoComplete(on_select=full_name_select)
    full_name_field = ft.Row(
        controls=[
            ft.Text("ФИО", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ft.Container(
                content=full_name_autocomplete,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=ft.border_radius.all(5),
                padding=ft.padding.only(5, 0, 0, 5),
                height=50,
                expand=True,
            ),
            navigation_controls,
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


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
            role_field,
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
    page.add(navigation_bar,form)


ft.app(target=main)
