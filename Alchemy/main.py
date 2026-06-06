# Импорт всех необходимых модулей и функций
from database import SessionLocal, engine, Base  # Настройки БД
from models import Author, Post, Comment  # ORM-модели (для прямого создания объектов)
from crud import *  # Все функции для работы с данными
from datetime import datetime  # Для работы с датами


def main():
    """Главная функция программы — демонстрация всех CRUD-операций"""

    # Создаём все таблицы в БД на основе моделей
    Base.metadata.create_all(bind=engine)

    # Создаём сессию для работы с БД
    db = SessionLocal()

    try:  # Блок try — выполняем операции, ловим возможные ошибки
        print("=== Блог ===\n")

        #СОЗДАНИЕ
        print("1. СОЗДАНИЕ АВТОРОВ")
        a1 = create_author(db, "Максим Дубровин", "maxim@example.com")  # Создаём первого автора
        a2 = create_author(db, "Екатерина Власова", "katya@example.com")  # Создаём второго
        print(f"   ✅ Созданы: {a1.name}, {a2.name}\n")

        print("2. СОЗДАНИЕ ПОСТОВ")
        p1 = create_post(db, "Как я путешествовал по Алтаю", "Рассказ о поездке в горы", a1.id, True)
        p2 = create_post(db, "Заметки о программировании", "Советы для начинающих", a1.id, False)
        p3 = create_post(db, "Рецепт домашнего хлеба", "Пошаговое руководство", a2.id, True)
        print(f"   ✅ Созданы: '{p1.title}', '{p2.title}', '{p3.title}'\n")

        print("3. ДОБАВЛЕНИЕ КОММЕНТАРИЕВ")
        add_comment(db, p1.id, "Андрей Смирнов", "Красивые места, завидую!")
        add_comment(db, p1.id, "Ольга Кузнецова", "Отличный рассказ, вдохновили!")
        add_comment(db, p1.id, "Дмитрий Морозов", "А какая погода была?")
        add_comment(db, p3.id, "Наталья Павлова", "Вкуснятина, спасибо за рецепт!")
        print("   ✅ Добавлено 4 комментария\n")

        #ОБНОВЛЕНИЕ
        print("4. ПУБЛИКАЦИЯ ЧЕРНОВИКА")
        update_post_status(db, p2.id, True)  # Меняем статус поста с False на True
        print(f"   ✅ Пост '{p2.title}' опубликован\n")

        #ЧТЕНИЕ
        print("5. ВСЕ ОПУБЛИКОВАННЫЕ ПОСТЫ")
        for post in get_published_posts(db):  # Получаем список опубликованных постов
            print(f"   📌 {post.title} (автор: {post.author.name})")
        print()

        print("6. ТОП АВТОРОВ ПО КОЛИЧЕСТВУ ПОСТОВ")
        top = get_top_authors_by_posts(db, 3)  # Получаем топ-3 авторов
        for i, (name, cnt) in enumerate(top, 1):
            print(f"   {i}. {name}: {cnt} пост(ов)")
        print()

        print("7. ПОИСК АВТОРА ПО EMAIL")
        author = get_author_by_email(db, "maxim@example.com")
        if author:
            print(f"   ✅ Найден: {author.name}\n")

        # Добавляем старый пост для демонстрации фильтрации по дате
        old = Post(
            title="Забытый черновик",
            content="Какой-то старый текст",
            author_id=a1.id,
            published=True,
            created_at=datetime(2024, 1, 1, 12, 0, 0)  # Дата в прошлом году
        )
        db.add(old)
        db.commit()

        print("8. ОПУБЛИКОВАННЫЕ ПОСТЫ ЗА СЕГОДНЯ")
        today = datetime.utcnow()  # Текущая дата и время
        posts_today = get_published_posts_by_date(db, today)
        if posts_today:
            for pt in posts_today:
                print(f"   📌 {pt.title}")
        else:
            print("   📭 Нет постов за сегодня")
        print()

        #МАССОВОЕ СОЗДАНИЕ
        print("9. МАССОВОЕ ДОБАВЛЕНИЕ АВТОРОВ")
        authors_data = [
            ("Артем Белов", "artem@example.com"),
            ("София Лебедева", "sofia@example.com"),
            ("Глеб Калинин", "gleb@example.com")
        ]
        new_authors = add_multiple_authors(db, authors_data)
        for a in new_authors:
            print(f"   ✅ Добавлен: {a.name} ({a.email})")
        print()

        #ЧТЕНИЕ С КОММЕНТАРИЯМИ
        print("10. ВЫВОД ПОСТА С КОММЕНТАРИЯМИ (ПОСТ №1)")
        result = get_post_with_comments(db, p1.id)
        if result:
            post, comments = result
            print(f"   📖 Пост: {post.title}")
            print(f"   💬 Комментарии ({len(comments)} шт.):")
            for c in comments:
                print(f"      - {c.author_name}: {c.text}")
        print()

        print("11. ВЫВОД ПОСТА С КОММЕНТАРИЯМИ (ПОСТ №3)")
        result3 = get_post_with_comments(db, p3.id)
        if result3:
            post, comments = result3
            print(f"   📖 Пост: {post.title}")
            print(f"   💬 Комментарии ({len(comments)} шт.):")
            for c in comments:
                print(f"      - {c.author_name}: {c.text}")

        print("\n" + "=" * 50)
        print("✅ ВСЕ ОПЕРАЦИИ ВЫПОЛНЕНЫ УСПЕШНО")
        print("=" * 50)

    except Exception as e:  # Если произошла ошибка
        print(f"❌ ОШИБКА: {e}")  # Выводим сообщение об ошибке
        db.rollback()  # Откатываем все изменения (транзакция не сохраняется)
    finally:  # Блок, который выполняется всегда
        db.close()  # Закрываем соединение с базой данных


# Точка входа в программу
if __name__ == "__main__":
    main()  # Запускаем главную функцию