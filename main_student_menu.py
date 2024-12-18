
import flet as ft
from datetime import date, timedelta
from db_connection import create_connection


def open(page: ft.Page, connection, group, fio):
    page.theme_mode = ft.ThemeMode.LIGHT
    main_text = ft.TextThemeStyle.HEADLINE_MEDIUM
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20


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

            # Получаем расписание
            schedule_data = cursor.fetchall()

            cursor.close()

            return schedule_data
        except Exception as err:
            print(f"Ошибка выполнения запроса: {err}")
            return []

    def show_info(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Пояснение"),
            content=ft.Text(f"Пояснение для {e.control.data}"),
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()


    # Title section
    title_text = ft.Text(f"Добро пожаловать {fio}", style=ft.TextThemeStyle.HEADLINE_LARGE)

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

    schedule_box = ft.Container(
        ft.Column([schedule_title, schedule_table]),
        border_radius=8,
        border=ft.border.all(1, "black"),
        padding=10,
        height=460,  # Установлена одинаковая высота для обоих контейнеров
        alignment=ft.alignment.top_left
    )

    # Task list section (Ближайшие задания)
    task_title = ft.Text("Ближайшие задания", style=main_text)

    task_list = ft.Column(
        controls=[
            ft.Row(
                [ft.Text("задание 1", expand=True), ft.IconButton(icon=ft.icons.INFO, on_click=show_info)],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),

        ],
        expand=True
    )


    task_box = ft.Container(
        ft.Column([task_title, task_list]),
        border_radius=8,
        border=ft.border.all(1, "black"),
        padding=10,
        expand=True,
        height=460,
        alignment=ft.alignment.top_right
    )

    # Main layout: two columns side by side
    main_layout = ft.Row(
        controls=[schedule_box, task_box],
        spacing=20,
        expand=True
    )


    page.add(title_column, main_layout)
