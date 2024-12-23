import flet as ft
from datetime import datetime, timedelta, date
from db_connection import Error
from datetime import date

def open(page: ft.Page, connection, id):
    group_value = ''
    disciplines = []

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

    def load_disciplines():
        nonlocal disciplines

        try:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT ts.subject FROM teacher t
            JOIN teacher_subjects ts ON t.idteacher = ts.teacher
            WHERE t.idteacher = %s
            """, (id,))
            rows = cursor.fetchall()
            disciplines = [row[0] for row in rows]

            disciplines = [ft.dropdown.Option(discipline) for discipline in disciplines]

            page.update()
            cursor.close()

        except Error as e:
            print(f"Ошибка при загрузке дисциплин: {e}")

    def save(e):
        try:
            cursor = connection.cursor()

            # 1. Добавляем задание
            cursor.execute(
                """
                INSERT INTO tasks (task_name, description, addition_date, due_time, teacher, `group`, subject)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (title_field.value, description_field.value, date.today(), datetime.strptime(date_f.value, '%d-%m-%Y'), id, group_value,
                 discipline_field.value)
            )

            # Получаем ID добавленного задания
            cursor.execute("SELECT LAST_INSERT_ID()")
            task_id = cursor.fetchone()[0]

            # 2. Получаем список студентов в группе
            cursor.execute("SELECT idstudent FROM student WHERE `group` = %s", (group_value,))
            students = cursor.fetchall()

            # 3. Добавляем студентов к задаче
            for student in students:
                cursor.execute("INSERT INTO student_tasks (student, task) VALUES (%s, %s)", (student[0], task_id))

            # 4. Создаем уведомление
            notification_name = f"Новое задание: {title_field.value}"
            notification_content = (
                f"Добавлено новое задание: {title_field.value}. Срок сдачи: {date_f.value}. "
                f"Описание: {description_field.value}"
            )
            cursor.execute(
                """
                INSERT INTO notification (name, time, content)
                VALUES (%s, NOW(), %s)
                """,
                (notification_name, notification_content)
            )

            # Получаем ID добавленного уведомления
            cursor.execute("SELECT LAST_INSERT_ID()")
            notification_id = cursor.fetchone()[0]

            # 5. Добавляем уведомление для каждого студента
            for student in students:
                cursor.execute(
                    """
                    INSERT INTO st_notification (student, notification, checked)
                    VALUES (%s, %s, 0)
                    """,
                    (student[0], notification_id)
                )

            # Уведомление об успехе
            snackbar.content = ft.Text("Задача добавлена")
            snackbar.open = True
            page.update()

            # Фиксируем изменения
            connection.commit()
            cursor.close()

        except Error as e:
            print(f"Ошибка при добавлении задачи или уведомлений: {e}")
            connection.rollback()



        except Error as e:
            print(f"Ошибка при загрузке дисциплин: {e}")

    def group_select(e):
        nonlocal group_value
        group_value = e.selection.value

    def date_change(e):
        date_f.value = e.control.value.strftime("%d-%m-%Y")
        page.update()


    load_disciplines()

    date_f = ft.TextField(read_only=True, width=200, value=date.today().strftime("%d-%m-%Y"),
                        border=ft.InputBorder.NONE, content_padding=10)
    date_field = ft.Container(ft.Row([
        date_f,
        ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(ft.DatePicker(on_change=date_change))
        ),
    ] ), border=ft.border.all(1, ft.colors.BLACK), border_radius=5)

    # Поля ввода
    group_autocomplete = ft.AutoComplete(on_select=group_select)
    group_field = ft.Row(
        controls=[
            ft.Text("Группа", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ft.Container(
                content=group_autocomplete,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=ft.border_radius.all(5),
                padding=ft.padding.only(5, 0, 0, 5),
                height=50,
                width=400
            ),
        ],
    )

    discipline_field = ft.Dropdown(label="Дисциплина", options=disciplines, expand=True)
    title_field = ft.TextField(label="Наименование", expand=True, max_length=45)
    description_field = ft.TextField(label="Описание", multiline=True, min_lines=5, expand=True)

    # Кнопка создания
    create_button = ft.ElevatedButton(text="Создать", expand=False, on_click=save)
    snackbar = ft.SnackBar(ft.Text(''))
    load_groups()
    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        group_field, date_field
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                discipline_field,
                title_field,
                description_field,
                ft.Row(
                    controls=[
                        create_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.START,
        ),
        snackbar
    )

