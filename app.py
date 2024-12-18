import flet as ft

import edit_user, add_user, main_student_menu, auth, schedule_edit, schedule, add_task
from db_connection import create_connection


def main(page: ft.Page):
    global navigation_bar
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.window.min_width = 1200
    page.window.min_height = 60
    group = ''
    fio = ''


    connection = create_connection()

    navigation_bar = ft.Container(
        bgcolor=ft.colors.GREY_400,
        padding=10
    )

    def page_switch(target="add mode page"):
        nonlocal group, fio
        page.clean()
        page.add(navigation_bar)
        if target == "edit mode page":
            edit_user.open(page, connection, page_switch)
        elif target == "add mode page":
            add_user.open(page, connection, page_switch)
        elif target == "main menu":
            main_student_menu.open(page, connection, group, fio)
        elif target == "schedule edit":
            schedule_edit.open(page, connection)
        elif target == "schedule view":
            schedule.open(page, connection, group)
        elif target == "add task":
            add_task.open(page)


    def callback(role, login=None):
        nonlocal group, fio
        if role == 'admin':
            navigation_bar.content = ft.Row([ft.IconButton(icon=ft.icons.PEOPLE, tooltip="Добавить пользователя",
                                                           on_click=lambda e: page_switch(target="add mode page")),
                                             ft.IconButton(icon=ft.icons.DATE_RANGE, tooltip="Редактировать расписание",
                                                           on_click=lambda e: page_switch(target="schedule edit"))],
                                            alignment=ft.MainAxisAlignment.CENTER)
        elif role == 'student':
            cursor = connection.cursor()
            cursor.execute("""SELECT s.`group`, s.full_name from 
                                accounts a
                                JOIN student s ON s.idstudent = a.idstudent
                                WHERE login = %s""",
                           (login,))
            group, fio = cursor.fetchone()
            navigation_bar.content = ft.Row([ft.IconButton(icon=ft.icons.CALENDAR_MONTH, tooltip="Расписание",
                                                           on_click=lambda e: page_switch(target="schedule view")),
                                             ft.IconButton(icon=ft.icons.HOME, tooltip="Главное меню",
                                                           on_click=lambda  e: page_switch(target="main menu"))],
                                            alignment=ft.MainAxisAlignment.CENTER)
        elif role == 'teacher':
            navigation_bar.content = ft.Row([ft.IconButton(icon=ft.icons.EDIT_DOCUMENT, tooltip="Добавление задания",
                                                           on_click=lambda e: page_switch(target="schedule view")),
                                             ft.IconButton(icon=ft.icons.TABLE_CHART_ROUNDED, tooltip="Главное меню",
                                                           on_click=lambda e: page_switch(target="main menu"))],
                                            alignment=ft.MainAxisAlignment.CENTER)

    auth.open(page, connection, page_switch, callback)


if __name__ == '__main__':
    ft.app(target=main)