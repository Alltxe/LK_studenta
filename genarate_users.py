from faker import Faker
import random
from werkzeug.security import generate_password_hash  # Для хеширования паролей
from db_connection import create_connection


fake = Faker("ru_RU")  # Русский язык


connection = create_connection()

def generate_test_data(num_students=50, num_teachers=10):
    cursor = connection.cursor()

    # Получаем все доступные группы
    cursor.execute("SELECT idgroups FROM st_groups")
    groups = [row[0] for row in cursor.fetchall()]

    # Получаем все доступные предметы
    cursor.execute("SELECT subject_name FROM subject")
    subjects = [row[0] for row in cursor.fetchall()]

    if not groups or not subjects:
        print("Нет данных для групп или предметов. Проверьте базу.")
        return

    # Генерация студентов
    for _ in range(num_students):
        full_name = fake.name()
        birth_date = fake.date_of_birth(minimum_age=16, maximum_age=60)
        group = random.choice(groups)
        login = fake.user_name()
        password = generate_password_hash("123")  # Статический пароль для теста

        # Добавляем студента в таблицу student
        cursor.execute(
            "INSERT INTO student (full_name, `group`, birth_date) VALUES (%s, %s, %s)",
            (full_name, group, birth_date)
        )
        cursor.execute("SELECT LAST_INSERT_ID()")
        student_id = cursor.fetchone()[0]

        # Добавляем учетную запись студента
        cursor.execute(
            "INSERT INTO accounts (login, password, role, idstudent) VALUES (%s, %s, %s, %s)",
            (login, password, "student", student_id)
        )

    # Генерация преподавателей
    for _ in range(num_teachers):
        full_name = fake.name()
        birth_date = fake.date_of_birth(minimum_age=15, maximum_age=60)
        phone_number = fake.phone_number()
        login = fake.user_name()
        password = generate_password_hash("teacherpass123")  # Статический пароль для теста

        # Добавляем преподавателя в таблицу teacher
        cursor.execute(
            "INSERT INTO teacher (full_name, birth_date, phone_number) VALUES (%s, %s, %s)",
            (full_name, birth_date, phone_number)
        )
        cursor.execute("SELECT LAST_INSERT_ID()")
        teacher_id = cursor.fetchone()[0]

        # Привязываем преподавателя к случайным предметам
        assigned_subjects = random.sample(subjects, k=random.randint(1, 3))  # 1-3 предмета
        for subject_id in assigned_subjects:
            cursor.execute(
                "INSERT INTO teacher_subjects (teacher, subject) VALUES (%s, %s)",
                (teacher_id, subject_id)
            )

        # Добавляем учетную запись преподавателя
        cursor.execute(
            "INSERT INTO accounts (login, password, role, idteacher) VALUES (%s, %s, %s, %s)",
            (login, password, "teacher", teacher_id)
        )

    # Сохраняем изменения
    connection.commit()
    cursor.close()
    print(f"Сгенерировано {num_students} студентов и {num_teachers} преподавателей.")


# Запуск генерации
generate_test_data(120, 10)
