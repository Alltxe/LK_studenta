import flet as ft
import datetime
from db_connection import Error

# Функция для подключения к базе данных и получения расписания для студента

# Основная функция Flet
def open(page: ft.Page, connection, group):
    # Получаем текущую дату и номер недели
    today = datetime.date.today()
    current_week_number = today.isocalendar()[1] + 1

    def get_day_schedule(group, selected_day):
        try:
            cursor = connection.cursor()

            # Получаем расписание для данной группы на текущую неделю
            query = """
            SELECT s.date, s.subject, s.location, s.class_type, t.full_name 
            FROM schedule s
            JOIN teacher t ON s.idteacher = t.idteacher
            WHERE s.group = %s AND DATE(s.date) = %s
            ORDER BY s.date
            """
            cursor.execute(query, (group, selected_day))

            # Получаем расписание
            schedule_data = cursor.fetchall()

            cursor.close()

            return schedule_data
        except Exception as err:
            print(f"Ошибка выполнения запроса: {err}")
            return []

    # Функция для получения диапазона дат недели
    def getDateRangeFromWeek(p_year, p_week):
        firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week)-1}-1', "%Y-W%W-%w").date()
        lastdayofweek = firstdayofweek + datetime.timedelta(days=6)
        return firstdayofweek, lastdayofweek

    # Получаем диапазон дат текущей недели
    firstdate, lastdate = getDateRangeFromWeek(str(today.year), current_week_number)

    # Форматируем диапазон дат для отображения
    current_week = ft.Text(value=f"{firstdate.strftime('%d-%m-%Y')} - {lastdate.strftime('%d-%m-%Y')}", size=16, weight=ft.FontWeight.BOLD)

    # Кнопки переключения недель
    prev_week_btn = ft.IconButton(ft.icons.ARROW_LEFT, on_click=lambda _: switch_week(-1))
    next_week_btn = ft.IconButton(ft.icons.ARROW_RIGHT, on_click=lambda _: switch_week(1))

    # Список дней недели на русском языке
    russian_weekdays = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }

    # Функция для получения дней недели с русскими названиями, исключая воскресенье
    def get_days_of_week(start_date):
        days = []
        for i in range(7):
            day = start_date + datetime.timedelta(days=i)
            if day.weekday() != 6:  # Исключаем воскресенье (6)
                days.append(f"{day.strftime('%d-%m-%Y')} {russian_weekdays[day.weekday()]}")
        return days

    # Получаем список дней недели (без воскресенья)
    days = get_days_of_week(firstdate)
    selected_day = days[0]  # День по умолчанию (вторник)

    # Левая часть: расписание на день
    schedule_header = ft.Text("Расписание на выбранный день", size=16, weight=ft.FontWeight.BOLD)
    schedule_content = ft.Column(
        controls=[ft.Text("Здесь будет отображаться расписание", size=14)],
        spacing=5,
        expand=True
    )

    # Функция для выбора дня
    def select_day(day):
        nonlocal selected_day
        selected_day = day
        update_days_list()  # Обновление списка дней
        schedule_content.controls.clear()  # Очищаем текущее расписание

        # Преобразуем выбранный день (строку) в дату
        selected_day_date = datetime.datetime.strptime(day.split()[0], "%d-%m-%Y").date()

        # Получаем расписание студента для выбранного дня
        student_schedule = get_day_schedule(group, selected_day_date)

        if not student_schedule:
            schedule_content.controls.append(ft.Text("Расписание не найдено", size=14))
        else:
            # Оформляем расписание в виде таблицы
            schedule_table = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Время", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("Дисциплина", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("Кабинет", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("Тип занятия", weight=ft.FontWeight.BOLD))
                ],
                rows=[]
            )

            for lesson in student_schedule:
                lesson_date, subject, location, class_type, teacher_name = lesson
                lesson_time = lesson_date.strftime('%H:%M')

                # Добавляем строку в таблицу для каждого занятия
                schedule_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(lesson_time)),
                    ft.DataCell(ft.Text(subject)),
                    ft.DataCell(ft.Text(location)),
                    ft.DataCell(ft.Text(class_type))
                ]))

            schedule_content.controls.append(schedule_table)

        page.update()  # Обновление страницы

    # Обновление списка дней с выделением выбранного
    def update_days_list():
        days_list.controls.clear()
        for day in days:
            days_list.controls.append(ft.Container(
                content=ft.Text(day, size=14),
                on_click=lambda e, d=day: select_day(d),
                bgcolor=ft.colors.GREY_300 if day == selected_day else ft.colors.GREY_200,
                padding=15,
                border_radius=5
            ))
        page.update()

    # Инициализация списка дней
    days_list = ft.ListView(expand=True, spacing=5)
    update_days_list()

    # Функция для переключения недель
    def switch_week(direction):
        nonlocal current_week_number
        nonlocal firstdate, lastdate
        current_week_number += direction
        firstdate, lastdate = getDateRangeFromWeek(str(today.year), current_week_number)
        current_week.value = f"{firstdate.strftime('%d.%m.%Y')} - {lastdate.strftime('%d.%m.%Y')}"
        days[:] = get_days_of_week(firstdate)
        update_days_list()
        page.update()

    # Строка с кнопками переключения недели
    week_row = ft.Row(
        controls=[
            prev_week_btn,
            current_week,
            next_week_btn
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Контейнер с расписанием
    schedule = ft.Container(
        content=ft.Column(controls=[schedule_header, schedule_content], expand=True),
        width=400,
        border=ft.border.all(1, ft.colors.GREY_400),
        padding=10,
        border_radius=5,
        expand=True
    )

    # Контейнер с днями недели и переключением недели
    days_col = ft.Container(
        content=ft.Column(
            controls=[week_row, days_list],
            expand=True
        ),
        width=300,
        border=ft.border.all(1, ft.colors.GREY_400),
        padding=10,
        border_radius=5,
        expand=True
    )

    # Главный макет
    form = ft.Column([ft.Row(
        controls=[schedule, days_col],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
    )], expand=True)

    page.add(form)

