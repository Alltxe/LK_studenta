from werkzeug.security import check_password_hash
import flet as ft

def open(page: ft.Page, connection, switch, callback):
    def login(e):
        username = username_field.value
        password = password_field.value

        cursor = connection.cursor()
        query = "SELECT * FROM accounts WHERE login = %s"
        cursor.execute(query, (username,))
        account = cursor.fetchone()
        cursor.close()

        if account and check_password_hash(account[1], password):
            role = account[4]
            callback(role, username)
            if role == 'teacher':
                switch(target="add task")
            elif role == 'student':
                switch(target="main menu")
            elif role == 'admin':
                switch(target="add mode page")
        else:
            snackbar = ft.SnackBar(content=ft.Text("Неправильный логин или пароль"))
            snackbar.open = True
            page.add(snackbar)

        page.update()
        return None

    username_field = ft.TextField(label="Логин", width=300)
    password_field = ft.TextField(label="Пароль", password=True, width=300, can_reveal_password=True)
    login_button = ft.ElevatedButton(text="Войти", on_click=login)

    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Авторизация", size=20, weight="bold"),
                username_field,
                password_field,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        width=400,
        height=400,
        padding=20,
        border_radius=10,
    )

    page.add(
        ft.Container(
            content=container,
            alignment=ft.alignment.center,
        )
    )