import flet as ft
from db_connection import create_connection, Error
import datetime

def open(page: ft.Page):
    connection = create_connection()
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
            cursor.execute("SELECT subject_name FROM subject")  # Получаем все дисциплины из таблицы `subject`
            rows = cursor.fetchall()
            disciplines = [row[0] for row in rows]

            disciplines = [ft.dropdown.Option(discipline) for discipline in disciplines]
            print(disciplines)

            page.update()
            cursor.close()

        except Error as e:
            print(f"Ошибка при загрузке дисциплин: {e}")

    def group_select(e):
        global group_value
        group_value = e.selection.value
        print(group_value)

    # Функция изменения даты
    def shift_date(e, delta):
        if not date.value:  # Если дата еще не выбрана, устанавливаем текущую дату
            current_date = datetime.date.today()
        else:
            current_date = datetime.datetime.strptime(date.value, "%Y-%m-%d").date()

        new_date = current_date + datetime.timedelta(days=delta)
        date.value = new_date.strftime("%Y-%m-%d")
        page.update()

    # Функция для обработки выбора даты в календаре
    def date_change(e):
        date.value = e.control.value.strftime("%Y-%m-%d")
        page.update()

    # Поле ввода группы (без изменений)
    group_autocomplete = ft.AutoComplete()
    group_field = ft.Column(
        controls=[
            ft.Text("Группа", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ft.Container(
                content=group_autocomplete,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=ft.border_radius.all(5),
                padding=ft.padding.only(5, 0, 0, 5),
                height=50,
                width=250,
            ),
        ],
    )

    # Поле даты и кнопки
    date = ft.TextField(width=200, read_only=True, value=datetime.date.today().strftime("%Y-%m-%d"))

    date_picker = ft.DatePicker(on_change=date_change)
    page.overlay.append(date_picker)  # Добавляем календарь в overlay страницы

    group_autocomplete = ft.AutoComplete(on_select=group_select)
    group_field = ft.Column(
        controls = [ft.Text("Группа", theme_style=ft.TextThemeStyle.BODY_LARGE),
            ft.Container(content=group_autocomplete,
                               border=ft.border.all(1,ft.colors.BLACK), border_radius=ft.border_radius.all(5),
                               padding=ft.padding.only(5,0,0,5), height=50, width=250)],)

    date_field = ft.Container(
        content=ft.Column([
            ft.Container(content=ft.Text("Дата", size=14), margin=ft.margin.only(50)),
            ft.Row([
                ft.IconButton(
                    icon=ft.icons.ARROW_LEFT,
                    on_click=lambda e: shift_date(e, -1)  # Уменьшаем дату на 1 день
                ),
                date,
                ft.IconButton(
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda e:page.open(ft.DatePicker(on_change=date_change))
                ),
                ft.IconButton(
                    icon=ft.icons.ARROW_RIGHT,
                    on_click=lambda e: shift_date(e, 1)  # Увеличиваем дату на 1 день
                ),
            ])
        ])
    )

    group_date_field = ft.Row(controls=[group_field, date_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # Таблица расписания
    def create_table_cell(text):
        return ft.Container(
            content=ft.Text(text, size=14),
            alignment=ft.alignment.center,
            border=ft.border.all(1, ft.colors.GREY_400),
            padding=10,
            expand=True,
        )

    def create_table_row(time="", subject="", room="", type_=""):
        return ft.Row(
            controls=[
                ft.TextField(border=ft.InputBorder.NONE, value=time),
                ft.Dropdown(options=disciplines),
                create_table_cell(room),
                create_table_cell(type_)
            ],
            spacing=0,
            expand=True
        )

    table_header = create_table_row("Время", "Дисциплина", "Кабинет", "Тип занятия")

    table_rows = [create_table_row(time = '08:20 - 09:40'),
                  create_table_row(time = '10:00 - 11:30'),
                  create_table_row(time = '11:45 - 13:15'),
                  create_table_row(time = '14:00 - 15:30'),
                  create_table_row(time = '15:45 - 17:15'),
                  create_table_row(time = '17:20 - 18:50'),
                  create_table_row(time = '18:55 - 20:25')]  # Пустые строки

    table = ft.Column(
        controls=[
            table_header,
            *table_rows
        ],
        spacing=0
    )

    # Общая структура страницы
    layout = ft.Column([
        ft.Divider(thickness=1),
        group_date_field,
        ft.Divider(thickness=1),
        table,
    ], spacing=20)

    load_groups()
    load_disciplines()
    page.add(layout)
    page.update()

if __name__ == '__main__':
    ft.app(target=open)