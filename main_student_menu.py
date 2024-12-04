import flet as ft


def open(page: ft.Page):
    main_text = ft.TextThemeStyle.HEADLINE_MEDIUM


    def show_info(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Пояснение"),
            content=ft.Text(f"Пояснение для {e.control.data}"),
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()


    # Title section
    title_text = ft.Text("Добро пожаловать USER", style=ft.TextThemeStyle.HEADLINE_LARGE)

    title_column = ft.Column(
        controls=[title_text],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Schedule section
    schedule_title = ft.Text("Расписание на завтра", style=main_text)
    schedule_table = ft.Column(
        controls=[
            ft.Row([ft.Text("..."), ft.Text("x-xxx")]),
            ft.Row([ft.Text("..."), ft.Text("x-xxx")]),
            ft.Row([ft.Text("..."), ft.Text("x-xxx")]),
        ],
        expand=True
    )

    schedule_box = ft.Container(
        ft.Column([schedule_title, schedule_table]),
        border_radius=8,
        border=ft.border.all(1, "black"),
        padding=10,
        expand=True,
        height=300,  # Установлена одинаковая высота для обоих контейнеров
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
        height=300,
        alignment=ft.alignment.top_right
    )

    # Main layout: two columns side by side
    main_layout = ft.Row(
        controls=[schedule_box, task_box],
        spacing=20,
        expand=True
    )

    # Add everything to the page
    page.add(title_column, main_layout)