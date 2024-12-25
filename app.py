import flet as ft

import edit_user, add_user, main_student_menu, auth, schedule_edit, schedule, add_task, task_info
from db_connection import create_connection


def main(page: ft.Page):
    global navigation_bar
    page.title = "Личный кабинет студента"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.window.min_width = 1200
    page.window.min_height = 720
    username = ''
    group = ''
    id = 0
    fio = ''


    def close_dialog(e):
        notifications_dialog.open = False
        page.update()

    notifications_dialog = ft.AlertDialog(
        title=ft.Text("Уведомления"),
        content=ft.Container(
            width=300,
            height=200,
            padding=10,
            bgcolor=ft.colors.WHITE,
        ),
        actions=[
            ft.TextButton("Закрыть", on_click=close_dialog)
        ],
    )

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
            edit_user.open(page, connection, page_switch, username)
        elif target == "add mode page":
            add_user.openn(page, connection, page_switch)
        elif target == "main menu":
            main_student_menu.open(page, connection, group, fio, id)
        elif target == "schedule edit":
            schedule_edit.open(page, connection)
        elif target == "schedule view":
            schedule.open(page, connection, group)
        elif target == "add task":
            add_task.open(page, connection, id)
        elif target == "task info":
            task_info.open(page, connection, id)

    def open_notifications(e):
        try:
            cursor = connection.cursor()
            query = """
            SELECT n.idnotification, n.name, n.time, sn.checked
            FROM st_notification sn
            JOIN notification n ON sn.notification = n.idnotification
            WHERE sn.student = %s
            ORDER BY n.time DESC
            """
            cursor.execute(query, (id,))
            notifications = cursor.fetchall()

            # Обновляем статус непрочитанных уведомлений
            unread_notifications = [notif[0] for notif in notifications if not notif[3]]  # ID непрочитанных уведомлений
            if unread_notifications:
                update_query = """
                UPDATE st_notification
                SET checked = 1
                WHERE student = %s AND notification IN (%s)
                """ % (id, ', '.join(map(str, unread_notifications)))
                cursor.execute(update_query)
                connection.commit()

            # Создаем ListView для отображения уведомлений
            notification_list = ft.ListView(
                expand=True,
                spacing=10,
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(f"{name} ({time.strftime('%d-%m-%Y %H:%M')})", weight=ft.FontWeight.BOLD),
                                ft.Text(
                                    "Статус: Прочитано" if checked else "Статус: Не прочитано",
                                    color="green" if checked else "red"
                                )
                            ],
                            spacing=5,
                        ),
                        padding=10,
                        border_radius=8,
                        border=ft.border.all(1, "black"),
                        bgcolor=ft.colors.GREY_200
                    )
                    for idnotification, name, time, checked in notifications
                ]
            )

            # Обновляем содержимое диалога уведомлений
            notifications_dialog.content = ft.Container(
                content=notification_list,
                width=400,
                height=300,
                padding=10,
                bgcolor=ft.colors.WHITE
            )

            # Открываем диалог
            page.overlay.append(notifications_dialog)
            notifications_dialog.open = True
            page.update()

            cursor.close()

        except Exception as err:
            print(f"Ошибка загрузки уведомлений: {err}")

            # Обновляем содержимое диалога уведомлений
            notifications_dialog.content = ft.Container(
                content=notification_list,
                width=400,
                height=300,
                padding=10,
                bgcolor=ft.colors.WHITE
            )

            # Открываем диалог
            page.overlay.append(notifications_dialog)
            notifications_dialog.open = True
            page.update()

        except Exception as err:
            print(f"Ошибка загрузки уведомлений: {err}")



    def callback(role, login=None):
        nonlocal group, fio, id, username
        if role == 'admin':
            navigation_bar.content = ft.Row([ft.IconButton(icon=ft.icons.PEOPLE, tooltip="Добавить пользователя",
                                                           on_click=lambda e: page_switch(target="add mode page")),
                                             ft.IconButton(icon=ft.icons.DATE_RANGE, tooltip="Редактировать расписание",
                                                           on_click=lambda e: page_switch(target="schedule edit"))],
                                            alignment=ft.MainAxisAlignment.CENTER)
            username = login
        elif role == 'student':
            cursor = connection.cursor()
            cursor.execute("""SELECT s.`group`, s.full_name, s.idstudent from 
                                accounts a
                                JOIN student s ON s.idstudent = a.idstudent
                                WHERE login = %s""",
                           (login,))
            group, fio, id = cursor.fetchone()
            cursor.close()
            navigation_bar.content = ft.Row([ft.IconButton(icon=ft.icons.CALENDAR_MONTH, tooltip="Расписание",
                                                           on_click=lambda e: page_switch(target="schedule view")),
                                             ft.IconButton(icon=ft.icons.HOME, tooltip="Главное меню",
                                                           on_click=lambda  e: page_switch(target="main menu")),
                                             ft.IconButton(icon=ft.icons.NOTIFICATIONS, on_click=open_notifications)],
                                            alignment=ft.MainAxisAlignment.CENTER)
        elif role == 'teacher':
            navigation_bar.content = ft.Row([ft.IconButton(icon=ft.icons.EDIT_DOCUMENT, tooltip="Добавление задания",
                                                           on_click=lambda e: page_switch(target="add task")),
                                             ft.IconButton(icon=ft.icons.TABLE_CHART_ROUNDED, tooltip="Выполнение заданий",
                                                           on_click=lambda e: page_switch(target="task info"))],
                                            alignment=ft.MainAxisAlignment.CENTER)
            cursor = connection.cursor()
            cursor.execute("""SELECT t.idteacher FROM accounts a JOIN teacher t ON a.idteacher = t.idteacher
                                WHERE login = %s""", (login,))
            id = cursor.fetchone()[0]
            cursor.close()

    auth.open(page, connection, page_switch, callback)


if __name__ == '__main__':
    ft.app(target=main)