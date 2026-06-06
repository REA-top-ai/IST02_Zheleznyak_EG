import os  # Модуль для работы с переменными окружения
from dotenv import load_dotenv  # Функция для загрузки переменных из .env файла
from sqlalchemy import create_engine  # Функция для создания движка подключения к БД
from sqlalchemy.orm import sessionmaker, declarative_base  # Фабрика сессий и базовый класс моделей

load_dotenv()  # Загружает переменные из файла .env в окружение

# Чтение параметров подключения из переменных окружения (со значениями по умолчанию)
DB_USER = os.getenv("DB_USER", "postgres")  # Имя пользователя БД
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")  # Пароль пользователя
DB_HOST = os.getenv("DB_HOST", "localhost")  # Хост (адрес сервера БД)
DB_PORT = os.getenv("DB_PORT", "5432")  # Порт PostgreSQL (стандартный 5432)
DB_NAME = os.getenv("DB_NAME", "blog_db")  # Имя базы данных

# Формирование строки подключения: postgresql://пользователь:пароль@хост:порт/имя_бд
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание движка (engine) — основного объекта для взаимодействия с БД
# echo=False отключает вывод всех SQL-запросов в консоль
engine = create_engine(DATABASE_URL, echo=False)

# Создание фабрики сессий (sessionmaker)
# bind=engine — привязываем к нашему движку
# autoflush=False — не отправлять изменения в БД автоматически
# autocommit=False — не фиксировать изменения автоматически
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Создание базового класса для всех ORM-моделей
# От него будут наследоваться все классы таблиц
Base = declarative_base()