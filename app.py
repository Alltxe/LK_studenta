import flet as ft
import edit_user, add_user

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.scroll = "adaptive"
    page.window.min_width = 450
    page.window.min_height = 600

    navigation_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.DATE_RANGE, tooltip="Календарь"),
                ft.IconButton(icon=ft.icons.HOME, tooltip="Главная"),
                ft.IconButton(icon=ft.icons.NOTIFICATIONS, tooltip="Уведомления"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor=ft.colors.GREY_400,
        padding=10
    )

    def page_switch(target="add mode page"):
        page.clean()
        page.add(navigation_bar)
        if target == "edit mode page":
            edit_user.open(page, page_switch)
        elif target == "add mode page":
            add_user.open(page, page_switch)


    page_switch()

if __name__ == '__main__':
    ft.app(target=main)