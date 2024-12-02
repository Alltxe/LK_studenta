from faker import Faker
from mysql.connector import connect, Error
from db_connection import create_connection

# Инициализация Faker для генерации случайных данных
fake = Faker("ru-RU")

def generate_subjects(num):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Программа, к которой привязаны все предметы
        program_name = "09.02.07"  # Единственная программа

        # Количество предметов для генерации
        num_subjects = num

        # Генерация данных для таблицы subject
        for _ in range(num_subjects):
            # Случайное название предмета
            subject_name = fake.job()

            try:
                # Вставка записи в таблицу subject
                query = """
                    INSERT INTO subject (subject_name, program) 
                    VALUES (%s, %s)
                """
                cursor.execute(query, (subject_name, program_name))
            except Error as e:
                print(f"Ошибка при добавлении предмета '{subject_name}': {e}")

        # Фиксация изменений
        connection.commit()
        print(f"Успешно добавлено {num_subjects} случайных предметов для программы '{program_name}'.")

    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Вызов функции для генерации предметов
generate_subjects(10)
