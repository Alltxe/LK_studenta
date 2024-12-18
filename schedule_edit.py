import flet as ft

from db_connection import Error
from datetime import datetime, timedelta, date



def open(page: ft.Page, connection):
    disciplines = []
    teachers = []
    group_value = ""
    page.theme_mode = ft.ThemeMode.LIGHT

    def load_schedule():
        try:
            cursor = connection.cursor()

            # Проверка, выбрана ли группа и дата
            if not group_value or not date_f.value:
                print("Пожалуйста, выберите группу и дату для загрузки расписания.")
                return

            # Выполнение SQL-запроса
            cursor.execute("""
                SELECT TIME_FORMAT(s.date, '%H:%i') AS time, s.subject, s.location, s.class_type, t.full_name 
                FROM schedule s
                JOIN teacher t ON s.idteacher = t.idteacher
                WHERE s.group = %s AND DATE(s.date) = %s
            """, (group_value, date_f.value))

            rows = cursor.fetchall()

            # Преобразование результатов запроса в словарь
            current_schedule = {row[0]: row for row in rows}

            # Очистка текущих строк таблицы
            table.controls.clear()
            table.controls.append(table_header)

            # Список временных интервалов
            time_slots = ["08:20", "10:00", "11:45", "14:00", "15:45", "17:20", "18:55"]

            # Добавление строк в таблицу
            for time_slot in time_slots:
                row = current_schedule.get(time_slot)  # Проверка наличия записи для временного интервала
                if row:
                    # Если данные для этого времени существуют в расписании
                    table_row = create_table_row(
                        time=f"{time_slot} - {(datetime.strptime(time_slot, '%H:%M') + timedelta(minutes=90)).strftime('%H:%M')}",
                        discipline=row[1],  # Дисциплина
                        room=row[2],  # Кабинет
                        type=row[3],  # Тип занятия
                        teacher=row[4]  # Преподаватель
                    )
                else:
                    # Если данные отсутствуют, добавляем пустую строку
                    table_row = create_table_row(
                        time=f"{time_slot} - {(datetime.strptime(time_slot, '%H:%M') + timedelta(minutes=90)).strftime('%H:%M')}",
                    )

                table.controls.append(table_row)

            # Обновление страницы
            page.update()
            cursor.close()

        except Error as e:
            print(f"Ошибка при загрузке расписания: {e}")

            # Обновление страницы
            page.update()
            cursor.close()
            print("Расписание успешно загружено!")

        except Error as e:
            print(f"Ошибка при загрузке расписания: {e}")

    def save_schedule(e):
        nonlocal table_rows
        try:
            cursor = connection.cursor()
            for row in table.controls[1::]:
                time_value = row.controls[0].value
                discipline_value = row.controls[1].value
                room_value = row.controls[2].value
                class_type_value = row.controls[3].value
                teacher_value = row.controls[4].value
                datetimee = f"{date_f.value} {time_value.split()[0]}:00"

                if not all([time_value, discipline_value, room_value, class_type_value, teacher_value]):
                    cursor.execute(
                        "DELETE FROM schedule WHERE `group` = %s AND date = %s",
                        (group_value, datetimee)
                    )
                    continue

                # Проверка, существует ли уже запись для данной группы и времени
                cursor.execute(
                    "SELECT * FROM schedule WHERE `group` = %s AND date = %s",
                    (group_value, datetimee)
                )
                result = cursor.fetchone()

                if result:
                    cursor.execute(
                        "UPDATE schedule SET location = %s, subject = %s, class_type = %s, "
                        "idteacher = (SELECT idteacher FROM teacher WHERE full_name=%s) "
                        "WHERE `group` = %s AND date = %s",
                        (room_value, discipline_value, class_type_value, teacher_value, group_value, datetimee)
                    )
                else:
                    cursor.execute(
                        "INSERT INTO schedule (date, location, subject, class_type, idteacher, `group`) "
                        "VALUES (%s, %s, %s, %s, (SELECT idteacher FROM teacher WHERE full_name=%s), %s)",
                        (datetimee, room_value, discipline_value, class_type_value, teacher_value, group_value)
                    )
            connection.commit()
            cursor.close()
        except Error as e:
            print(f"Ошибка при сохранении расписания: {e}")

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
            cursor.execute("SELECT subject_name FROM subject")
            rows = cursor.fetchall()
            disciplines = [row[0] for row in rows]

            disciplines = [ft.dropdown.Option(discipline) for discipline in disciplines]

            page.update()
            cursor.close()

        except Error as e:
            print(f"Ошибка при загрузке дисциплин: {e}")

    def load_teachers():
        nonlocal teachers

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT full_name FROM teacher")
            rows = cursor.fetchall()
            teachers = [row[0] for row in rows]

            teachers = [ft.dropdown.Option(teacher) for teacher in teachers]

            page.update()
            cursor.close()

        except Error as e:
            print(f"Ошибка при загрузке дисциплин: {e}")

    def group_select(e):
        global group_value
        group_value = e.selection.value

    # Функция изменения даты
    def shift_date(e, delta):
        if not date_f.value:  # Если дата еще не выбрана, устанавливаем текущую дату
            current_date = date.today()
        else:
            current_date = datetime.strptime(date_f.value, "%Y-%m-%d").date()

        new_date = current_date + timedelta(days=delta)
        date_f.value = new_date.strftime("%Y-%m-%d")
        load_schedule()
        page.update()

    # Функция для обработки выбора даты в календаре
    def date_change(e):
        date_f.value = e.control.value.strftime("%Y-%m-%d")
        page.update()

    def group_select(e):
        nonlocal group_value
        group_value = e.selection.value
        load_schedule()

    group_autocomplete = ft.AutoComplete(on_select=group_select)
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
    date_f = ft.TextField(width=200, read_only=True, value=date.today().strftime("%Y-%m-%d"),
                        border=ft.InputBorder.NONE, content_padding= 10)


    date_field = ft.Container(
        content=ft.Column([
            ft.Container(content=ft.Text("Дата", size=14), margin=ft.margin.only(50)),
            ft.Row([
                ft.IconButton(
                    icon=ft.icons.ARROW_LEFT,
                    on_click=lambda e: shift_date(e, -1)  # Уменьшаем дату на 1 день
                ),
                ft.Container(ft.Row([
                    date_f,
                    ft.IconButton(
                        icon=ft.icons.CALENDAR_MONTH,
                        on_click=lambda e: page.open(ft.DatePicker(on_change=date_change))
                    ),
                ]), border=ft.border.all(1,ft.colors.BLACK),
                    border_radius=5),
                ft.IconButton(
                    icon=ft.icons.ARROW_RIGHT,
                    on_click=lambda e: shift_date(e, 1)  # Увеличиваем дату на 1 день
                ),
            ]),
        ])
    )

    group_date_field = ft.Row(controls=[group_field, date_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # Таблица расписания
    def create_table_cell(text, expand = True, width = 350):
        return ft.Container(
            content=ft.Text(text, size=14),
            alignment=ft.alignment.center,
            border=ft.border.all(1, ft.colors.GREY_400),
            padding=10,
            expand=expand,
            width = width,
        )

    def create_table_row(time="", discipline="", room="", type="", teacher=""):
        nonlocal disciplines
        table_row = ft.Row(
            controls=[
                ft.TextField(border_radius=0, value=time, text_size=14, expand=True, border_color=ft.colors.GREY_400),
                ft.Dropdown(options=disciplines,border_radius=0, width=350, border_color=ft.colors.GREY_400, icon=None, value=discipline),
                ft.TextField(border_radius=0, text_size=14, expand=True, border_color=ft.colors.GREY_400, value=room),
                ft.Dropdown(border_radius=0, width=250, border_color=ft.colors.GREY_400, value=type,
                            options=[ft.dropdown.Option(option) for option in ['Лекция', 'Лабораторная работа', 'Практическая работа']]),
                ft.Dropdown(options=teachers,border_radius=0, width=350, border_color=ft.colors.GREY_400, icon=None, value=teacher),
            ],
            spacing=10,
            expand=True
        )
        return table_row


    table_header = ft.Row(controls=[
        create_table_cell('Время'),
        create_table_cell('Дисциплина', False),
        create_table_cell('Кабинет'),
        create_table_cell('Тип занятия', False, 250),
        create_table_cell('Преподаватель', False)
    ])
    load_disciplines()
    load_teachers()

    table_rows = [create_table_row(time = '08:20 - 09:50'),
                  create_table_row(time = '10:00 - 11:30'),
                  create_table_row(time = '11:45 - 13:15'),
                  create_table_row(time = '14:00 - 15:30'),
                  create_table_row(time = '15:45 - 17:15'),
                  create_table_row(time = '17:20 - 18:50'),
                  create_table_row(time = '18:55 - 20:25')]

    table = ft.Column(
        controls=[
            table_header,
            *table_rows
        ],
        spacing=0
    )

    save_btn = ft.ElevatedButton(text="Добавить/изменить", on_click=save_schedule)

    # Общая структура страницы
    layout = ft.Column([
        ft.Divider(thickness=1),
        group_date_field,
        ft.Divider(thickness=1),
        table,
        save_btn,
    ], spacing=10)

    load_groups()

    page.add(layout)
    page.update()