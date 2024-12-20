
import flet as ft
from datetime import date, timedelta



def open(page: ft.Page, connection, group, fio, id):
    page.theme_mode = ft.ThemeMode.LIGHT
    main_text = ft.TextThemeStyle.HEADLINE_MEDIUM
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    def get_day_schedule(selected_day):
        try:
            cursor = connection.cursor()

            query = """
            SELECT date, subject, location, class_type
            FROM schedule 
            WHERE `group` = %s AND DATE(date) = %s
            ORDER BY date
            """
            cursor.execute(query, (group, selected_day))
            schedule_data = cursor.fetchall()
            cursor.close()
            return schedule_data
        except Exception as err:
            print(f"Ошибка выполнения запроса: {err}")
            return []

    # Загрузка ближайших заданий
    def get_upcoming_tasks():
        try:
            cursor = connection.cursor()
            query = """
            SELECT t.task_name, t.due_time, t.description, s.status
            FROM tasks t
            LEFT JOIN student_tasks s ON s.task = t.idtasks AND s.student = %s
            WHERE t.`group` = %s AND t.due_time >= CURDATE()
            ORDER BY t.due_time ASC
            """
            cursor.execute(query, (id, group))
            tasks_data = cursor.fetchall()
            cursor.close()
            return tasks_data
        except Exception as err:
            print(f"Ошибка получения заданий: {err}")
            return []

    def show_info(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Детали задания"),
            content=ft.Text(f"Детальная информация: {e.control.data}"),
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    # Title section
    title_text = ft.Text(f"Добро пожаловать, {fio}", style=ft.TextThemeStyle.HEADLINE_LARGE)

    title_column = ft.Column(
        controls=[title_text],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Schedule section
    schedule_title = ft.Text("Расписание на завтра", style=main_text)
    schedule_table = ft.DataTable(
        expand=True,
        columns=[
            ft.DataColumn(ft.Text("Время", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Дисциплина", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Кабинет", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Тип занятия", weight=ft.FontWeight.BOLD))
        ],
        rows=[],
    )

    student_schedule = get_day_schedule(date.today() + timedelta(1))
    for lesson in student_schedule:
        lesson_date, subject, location, class_type = lesson
        lesson_time = lesson_date.strftime('%H:%M')

        schedule_table.rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(lesson_time)),
            ft.DataCell(ft.Text(subject)),
            ft.DataCell(ft.Text(location)),
            ft.DataCell(ft.Text(class_type))
        ]))

    separator = ft.Divider(height=2, thickness=2)

    schedule_box = ft.Container(
        schedule_table,
        border_radius=8,
        border=ft.border.all(1, "black"),
        padding=10,
        height=460,
        alignment=ft.alignment.top_left
    )

    # Task list section (Ближайшие задания)
    # Task list section (Ближайшие задания)
    task_title = ft.Text("Ближайшие задания", style=main_text)

    task_list = ft.ListView(expand=True, spacing=10)

    # Загрузка ближайших заданий
    upcoming_tasks = get_upcoming_tasks()
    for task_name, deadline, descripton, status in upcoming_tasks:
        status_text = "Выполнено" if status else "Не выполнено"
        deadline_text = deadline.strftime('%d-%m-%Y')
        task_row = ft.Row(
            controls=[
                ft.Text(f"{task_name} (до {deadline_text})", expand=True),
                ft.Text(status_text, color="green" if status else "red"),
                ft.IconButton(
                    icon=ft.icons.INFO,
                    on_click=show_info,
                    data=descripton
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        task_list.controls.append(task_row)

    task_box = ft.Container(
        task_list,
        border_radius=8,
        border=ft.border.all(1, "black"),
        padding=10,
        height=460,  # Высота, в которой можно прокручивать задания
        alignment=ft.alignment.top_right,
    )


    main_layout = ft.Column([
        title_column,
        separator,
        ft.Row(
        controls=[
            ft.Column([
                schedule_title, schedule_box
            ]),
            ft.Column([
                task_title, task_box
            ], expand=True)
        ],
        spacing=20,
        )],
    spacing=10)


    page.add(main_layout)
