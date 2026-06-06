# Импорт типов для аннотаций и функций SQLAlchemy
from sqlalchemy.orm import Session  # Тип для сессии БД
from sqlalchemy import func, desc  # func — агрегатные функции SQL, desc — сортировка по убыванию
from models import Author, Post, Comment  # Импорт моделей таблиц
from datetime import datetime  # Для работы с датами

#СОЗДАНИЕ

def create_author(session: Session, name: str, email: str) -> Author:
    """Создаёт нового автора в базе данных"""
    author = Author(name=name, email=email)  # Создаём объект автора
    session.add(author)  # Добавляем объект в сессию (готовим к сохранению)
    session.commit()  # Фиксируем изменения — сохраняем в БД
    session.refresh(author)  # Обновляем объект (подтягиваем сгенерированный БД id)
    return author  # Возвращаем созданного автора

def create_post(session: Session, title: str, content: str, author_id: int, published: bool = False) -> Post:
    """Создаёт новый пост"""
    post = Post(title=title, content=content, author_id=author_id, published=published)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

def add_comment(session: Session, post_id: int, author_name: str, text: str) -> Comment:
    """Добавляет комментарий к посту"""
    comment = Comment(post_id=post_id, author_name=author_name, text=text)
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment

def add_multiple_authors(session: Session, authors_list: list) -> list:
    """Добавляет нескольких авторов списком (массовое создание)"""
    new_authors = []  # Пустой список для хранения созданных авторов
    for name, email in authors_list:  # Перебираем каждый кортеж (имя, email)
        author = Author(name=name, email=email)  # Создаём автора
        session.add(author)  # Добавляем в сессию
        new_authors.append(author)  # Сохраняем в список
    session.commit()  # Сохраняем всех одним коммитом
    for author in new_authors:  # Обновляем каждого автора
        session.refresh(author)  # Чтобы получить id
    return new_authors

#ЧТЕНИЕ

def get_author_by_email(session: Session, email: str) -> Author | None:
    """Ищет автора по email. Возвращает первого найденного или None"""
    return session.query(Author).filter(Author.email == email).first()

def get_author_by_name(session: Session, name: str) -> Author | None:
    """Ищет автора по имени"""
    return session.query(Author).filter(Author.name == name).first()

def get_published_posts(session: Session, limit: int = 10) -> list:
    """Возвращает опубликованные посты (не более limit штук)"""
    return session.query(Post).filter(Post.published == True).limit(limit).all()

def get_posts_by_author(session: Session, author_id: int, limit: int = 10) -> list:
    """Возвращает посты конкретного автора"""
    return session.query(Post).filter(Post.author_id == author_id).limit(limit).all()

def get_published_posts_by_date(session: Session, date: datetime, limit: int = 10) -> list:
    """Возвращает опубликованные посты за конкретный день"""
    # Начало дня (00:00:00)
    start = datetime(date.year, date.month, date.day, 0, 0, 0)
    # Конец дня (23:59:59)
    end = datetime(date.year, date.month, date.day, 23, 59, 59)
    return session.query(Post)\
        .filter(Post.published == True)\
        .filter(Post.created_at >= start, Post.created_at <= end)\
        .limit(limit).all()

def get_post_with_comments(session: Session, post_id: int):
    """Возвращает пост и все его комментарии в виде кортежа (post, comments)"""
    post = session.query(Post).filter(Post.id == post_id).first()  # Ищем пост
    if not post:  # Если пост не найден
        return None
    return post, post.comments  # Возвращаем пост и его комментарии (связь подгружается автоматически)

def get_top_authors_by_posts(session: Session, limit: int = 5) -> list:
    """Возвращает топ авторов по количеству написанных постов"""
    return (
        session.query(Author.name, func.count(Post.id).label("post_count"))
        .join(Post)  # JOIN с таблицей posts (неявно по внешнему ключу)
        .group_by(Author.id)  # Группируем по автору
        .order_by(desc("post_count"))  # Сортируем по убыванию
        .limit(limit)
        .all()
    )

#ОБНОВЛЕНИЕ

def update_post_status(session: Session, post_id: int, published: bool) -> bool:
    """Обновляет статус публикации поста. Возвращает True, если пост найден и обновлён"""
    post = session.query(Post).filter(Post.id == post_id).first()  # Ищем пост
    if not post:  # Если пост не найден
        return False
    post.published = published  # Меняем значение поля
    session.commit()  # Сохраняем изменения
    return True

#УДАЛЕНИЕ

def delete_author(session: Session, author_id: int) -> bool:
    """Удаляет автора. Каскадно удаляются все его посты и комментарии"""
    author = session.query(Author).filter(Author.id == author_id).first()
    if not author:
        return False
    session.delete(author)  # Удаляем объект
    session.commit()
    return True

def delete_post(session: Session, post_id: int) -> bool:
    """Удаляет пост. Каскадно удаляются все его комментарии"""
    post = session.query(Post).filter(Post.id == post_id).first()
    if not post:
        return False
    session.delete(post)
    session.commit()
    return True

def delete_comment(session: Session, comment_id: int) -> bool:
    """Удаляет комментарий"""
    comment = session.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        return False
    session.delete(comment)
    session.commit()
    return True