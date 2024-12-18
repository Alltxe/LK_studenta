import flet as ft

def open(page: ft.Page):
    page.title = "Создание задания для преподавателя"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Поля ввода
    group_field = ft.TextField(label="Группа", expand=True)
    date_field = ft.TextField(label="Дата", expand=True, suffix=ft.Icon(ft.icons.CALENDAR_TODAY))
    discipline_field = ft.TextField(label="Дисциплина", expand=True)
    title_field = ft.TextField(label="Наименование", expand=True)
    description_field = ft.TextField(label="Описание", multiline=True, min_lines=3, max_lines=5, expand=True)

    # Кнопка создания
    create_button = ft.ElevatedButton(text="Создать", expand=False)

    # Основной макет
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(controls=[group_field], expand=1),
                            ft.Column(controls=[date_field], expand=1)
                        ],
                        spacing=20
                    ),
                    discipline_field,
                    title_field,
                    description_field,
                    ft.Row(
                        controls=[
                            create_button
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            border=ft.border.all(1, ft.colors.GREY_400),
            border_radius=10,
            padding=20,
            expand=True
        )
    )

