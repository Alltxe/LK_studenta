import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error
import os

def create_connection():
    """Создает подключение к базе данных, используя конфигурацию из .env файла."""
    load_dotenv()  # Загружаем переменные окружения из .env файла

    try:
        # Подключение к базе данных с использованием переменных окружения
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),  # Значение по умолчанию "localhost"
            user=os.getenv("DB_USER"),  # Переменная окружения для пользователя
            password=os.getenv("DB_PASSWORD"),  # Переменная окружения для пароля
            database=os.getenv("DB_NAME")  # Переменная окружения для базы данных
        )
        return connection

    except Error as e:
        print("Ошибка при подключении к базе данных:", e)
        return None
