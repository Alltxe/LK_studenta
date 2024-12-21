import flet as ft
from datetime import date
from db_connection import Error
from werkzeug.security import generate_password_hash


def open(page: ft.Page, connection, switch=None):
    disciplines = []
    group_value = ""
    records = []

    user_id = None
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
        nonlocal records
        try:
            cursor = connection.cursor()
            query = "SELECT idstudent, full_name FROM student where `group` = %s"
            cursor.execute(query, (group,))
            records = cursor.fetchall()
            full_name_autocomplete.suggestions = [ft.AutoCompleteSuggestion(key=student[1], value=student[1])
                                                  for student in records]
            page.update()

        except Error as e:
            print(f"Ошибка при загрузке студентов: {e}")

    def load_teachers():
        nonlocal records
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
        date_f.value = ""
        phone_field.value = ""
        discipline_dropdown.value = None
        disciplines.clear()
        page.update()

    # Контейнер для Chip элементов
    chips_container = ft.Row(
        controls=[],
        wrap=True,
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
            load_teachers()
        else:
            full_name_autocomplete.suggestions = []
            disciplines_section.visible = False
            group_field.visible = True
            phone_field.visible = False
            disciplines.clear()
            update_disciplines_display()
        page.update()

    def date_change(e):
        date_f.value = e.control.value.strftime("%Y-%m-%d")
        page.update()

    def group_select(e):
        nonlocal group_value
        group_value = e.selection.value
        load_students_from_group(group_value)


    def full_name_select(e):
        global full_name
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
            nonlocal disciplines, user_id
            login_field.value, date_f.value, user_id = records[index][0:3:]
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

    def update_user(e):
        nonlocal user_id

        if not user_id:
            bottom_attention("Пользователь не найден")
            return

        if not role_field.value:
            bottom_attention("Роль не выбрана")
            return

        cursor = connection.cursor()
        role = role_field.value
        login = login_field.value
        password = password_field.value
        birth_date = date_f.value
        phone_number = phone_field.value
        if role == "Студент":

            query = """
                UPDATE student
                SET full_name = %s, `group` = %s, birth_date = %s
                WHERE idstudent = %s
            """
            cursor.execute(query, (full_name, group_value, birth_date, user_id))

            query = """
                UPDATE accounts
                SET login = %s
                WHERE idstudent = %s
            """
            cursor.execute(query, (login, user_id))

        elif role == "Преподаватель":

            query = """
                UPDATE teacher
                SET full_name = %s, birth_date = %s, phone_number = %s
                WHERE idteacher = %s
            """
            cursor.execute(query, (full_name, birth_date, phone_number, user_id))

            query = """
                UPDATE accounts
                SET login = %s
                WHERE idteacher = %s
            """
            cursor.execute(query, (login, user_id))

            # Обновляем дисциплины преподавателя
            cursor.execute("DELETE FROM teacher_subjects WHERE teacher = %s", (user_id,))
            query = "INSERT INTO teacher_subjects (teacher, subject) VALUES (%s, %s)"
            for discipline in disciplines:
                cursor.execute(query, (user_id, discipline))

        if password:
            hashed_password = generate_password_hash(password)
            query = """
                UPDATE accounts
                SET login = %s, password = %s
                WHERE idstudent = %s OR idteacher = %s
            """
            cursor.execute(query, (login, hashed_password, user_id, user_id))


        connection.commit()
        cursor.close()
        bottom_attention("Данные успешно обновлены")
        page.update()

    def delete_user(e):
        cursor = connection.cursor()
        try:
            if role_field.value == "Преподаватель":
                cursor.execute("DELETE FROM teacher WHERE `idteacher` = %s", (user_id,))
            elif role_field.value == "Студент":
                cursor.execute("DELETE FROM student WHERE `idstudent` = %s", (user_id,))
            connection.commit()
            cursor.close()
            bottom_attention("Пользватель удален успешно")
            clear_page()
            page.update()
        except Error as e:
            print(e)

    discipline_dropdown = ft.Dropdown(
        label="Выберите дисциплину",
        expand=False, icon_size=0,
    )
    add_btn = ft.ElevatedButton(text="Добавить", on_click=add_discipline)

    # Элементы формы
    role_field = ft.Dropdown(
        options=[
            ft.dropdown.Option("Студент"),
            ft.dropdown.Option("Преподаватель"),
        ],
        label="Роль",
        on_change=on_role_change,
        width=431
    )
    group_autocomplete = ft.AutoComplete(on_select=group_select)
    group_field = ft.Row(
        controls = [ft.Text("Группа", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ft.Container(content=group_autocomplete,
                               border=ft.border.all(1,ft.colors.BLACK), border_radius=ft.border_radius.all(5),
                               padding=ft.padding.only(5,0,0,5), height=50, expand=True)],
        visible=False)

    date_f = date_f = ft.TextField(hint_text='Дата', read_only=True, width=200, value=date.today().strftime("%d-%m-%Y"),
                                   border=ft.InputBorder.NONE, content_padding=10, expand=True)
    date_field = ft.Container(ft.Row([
        date_f,
        ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(ft.DatePicker(on_change=date_change))
        ),
    ], width=300), border=ft.border.all(1, ft.colors.BLACK), border_radius=5)
    login_field = ft.TextField(label="Логин", max_length=45)
    password_field = ft.TextField(label="Пароль", password=True, can_reveal_password=True, max_length=45)
    phone_field = ft.TextField(label="Номер телефона", max_length=20, visible=False)
    save_btn = ft.ElevatedButton(text="Изменить", on_click=update_user)
    mode_switch_btn = ft.ElevatedButton(text="Добавление", on_click=lambda e:switch(target="add mode page"))
    delete_btn = ft.ElevatedButton(text="Удалить", bgcolor=ft.colors.RED_400,
                                   color = ft.colors.WHITE, on_click=delete_user)

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
                                        on_change=date_change
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


    form = ft.Column(
        controls=[
            ft.Row(
                controls=[role_field, mode_switch_btn],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            group_field,
            ft.Row([ft.Text("Дата рождения", theme_style=ft.TextThemeStyle.BODY_LARGE), date_field]),
            login_field,
            password_field,
            full_name_field,
            phone_field,
            disciplines_section,
            ft.Row(controls=[save_btn, delete_btn],
                   alignment= ft.MainAxisAlignment.SPACE_BETWEEN),
            snackbar,
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=False,
    )


    load_disciplines()
    load_groups()
    page.add(form)
