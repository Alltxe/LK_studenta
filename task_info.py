import flet as ft
from db_connection import Error


def open(page: ft.Page, connection, id):
    group_value = ""
    tasks = []
    disciplines = []

    # Функция для загрузки данных в таблицу
    def load_data():
        nonlocal tasks
        try:
            table.columns.clear()
            table.rows.clear()

            # Добавляем колонку "Студент" в начало
            table.columns.append(ft.DataColumn(ft.Container(ft.Text("Студент"), width=150)))

            # Создаём курсор
            cursor = connection.cursor()

            # Загружаем список заданий для выбранной группы и дисциплины
            cursor.execute(
                """
                SELECT t.idtasks, t.task_name 
                FROM tasks t 
                WHERE t.`group` = %s AND t.subject = %s
                """,
                (group_value, discipline_field.value),
            )
            tasks = cursor.fetchall()

            # Добавляем названия заданий в колонки
            for task in tasks:
                table.columns.append(
                    ft.DataColumn(ft.Container(ft.Text(task[1]), width=120))
                )

            # Загружаем список студентов с их статусами заданий одним запросом
            cursor.execute(
                """
                SELECT s.idstudent, s.full_name, t.idtasks, IFNULL(st.status, 0) AS status
                FROM student s
                CROSS JOIN tasks t ON t.`group` = s.`group`
                LEFT JOIN student_tasks st ON st.student = s.idstudent AND st.task = t.idtasks
                WHERE t.subject = %s AND t.`group` = %s
                ORDER BY s.idstudent, t.idtasks
                """,
                (discipline_field.value, group_value),
            )
            results = cursor.fetchall()

            # Организуем данные в словарь: {student_id: {task_id: status}}
            data = {}
            for student_id, full_name, task_id, status in results:
                if student_id not in data:
                    data[student_id] = {"name": full_name, "tasks": {}}
                data[student_id]["tasks"][task_id] = status

            # Заполняем таблицу
            for student_id, student_data in data.items():
                cells = [ft.DataCell(ft.Container(ft.Text(student_data["name"]), width=150))]

                for task in tasks:
                    task_id = task[0]
                    status_value = data[student_id]["tasks"].get(task_id, 0)

                    # Функция для сохранения статуса
                    def save_status(e, s_id=student_id, t_id=task_id):
                        new_status = 1 if e.control.value else 0
                        try:
                            cursor = connection.cursor()
                            cursor.execute(
                                "SELECT * FROM student_tasks WHERE student = %s AND task = %s",
                                (s_id, t_id),
                            )
                            result = cursor.fetchone()

                            if result:
                                cursor.execute(
                                    """
                                    UPDATE student_tasks 
                                    SET status = %s
                                    WHERE student = %s AND task = %s
                                    """,
                                    (new_status, s_id, t_id),
                                )
                            else:
                                cursor.execute(
                                    """
                                    INSERT INTO student_tasks (student, task, status) 
                                    VALUES (%s, %s, %s)
                                    """,
                                    (s_id, t_id, new_status),
                                )
                            connection.commit()
                            print(f"Статус сохранён: student={s_id}, task={t_id}, status={new_status}")
                        except Error as err:
                            print(f"Ошибка при сохранении статуса: {err}")

                    checkbox = ft.Checkbox(
                        value=bool(status_value), on_change=save_status
                    )
                    cells.append(ft.DataCell(checkbox))

                table.rows.append(ft.DataRow(cells))

            # Обновляем страницу
            page.update()
            cursor.close()

        except Error as e:
            print(f"Ошибка при загрузке данных: {e}")

    # Загрузка групп из базы данных
    def load_groups():
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT idgroups FROM st_groups")
            rows = cursor.fetchall()
            groups = [row[0] for row in rows]

            group_autocomplete.suggestions = [
                ft.AutoCompleteSuggestion(key=group, value=group) for group in groups
            ]

            cursor.close()
            page.update()
        except Error as e:
            print(f"Ошибка при загрузке групп: {e}")

    # Загрузка дисциплин из базы данных
    def load_disciplines():
        nonlocal disciplines
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT ts.subject 
                FROM teacher t 
                JOIN teacher_subjects ts ON t.idteacher = ts.teacher 
                WHERE t.idteacher = %s
                """,
                (id, ),
            )
            rows = cursor.fetchall()
            disciplines = [ft.dropdown.Option(row[0]) for row in rows]
            discipline_field.options = disciplines
            cursor.close()
            page.update()
        except Error as e:
            print(f"Ошибка при загрузке дисциплин: {e}")

    # Обработчик выбора группы
    def group_select(e):
        nonlocal group_value
        group_value = e.selection.value
        load_data()

    # Поля интерфейса
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
                width=400,
            ),
        ],
    )

    discipline_field = ft.Dropdown(
        label="Дисциплина", width=300, options=disciplines, on_change=lambda _: load_data()
    )

    # Таблица с данными
    table = ft.DataTable(
        border=ft.border.all(1, "black"),
        vertical_lines=ft.BorderSide(1, "black"),
        horizontal_lines=ft.BorderSide(1, "black"),
        columns=[ft.DataColumn(ft.Container(ft.Text("Выберите дисциплину и группу"), width=150))],
    )

    # Инициализация данных
    load_groups()
    load_disciplines()

    # Добавление элементов на страницу
    page.add(
        ft.Row(
            [group_field, discipline_field],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Row([table], scroll=ft.ScrollMode.ADAPTIVE),
    )
