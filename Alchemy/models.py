# Импорт типов колонок из SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship  # Для создания связей между таблицами
from datetime import datetime  # Для работы с датой и временем
from database import Base  # Базовый класс для моделей


# Модель таблицы "authors" (авторы)
class Author(Base):
    __tablename__ = "authors"  # Имя таблицы в базе данных

    # Поле id — первичный ключ, автоинкремент, индекс для быстрого поиска
    id = Column(Integer, primary_key=True, index=True)
    # Поле name — строка до 100 символов, не может быть пустым, уникальное
    name = Column(String(100), nullable=False, unique=True)
    # Поле email — строка до 150 символов, не может быть пустым, уникальное
    email = Column(String(150), nullable=False, unique=True)
    # Поле created_at — дата и время создания, по умолчанию текущее время UTC
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связь с таблицей Post (один автор — много постов)
    # back_populates указывает на обратную связь в модели Post
    # cascade="all, delete-orphan" — при удалении автора удаляются все его посты
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")


# Модель таблицы "posts"
class Post(Base):
    __tablename__ = "posts"  # Имя таблицы

    id = Column(Integer, primary_key=True, index=True)  # Первичный ключ
    title = Column(String(200), nullable=False)  # Заголовок поста
    content = Column(Text, nullable=False)  # Содержимое поста
    published = Column(Boolean, default=False)  # Статус публикации (по умолчанию false)
    created_at = Column(DateTime, default=datetime.utcnow)  # Дата создания
    # Внешний ключ: ссылается на id из таблицы authors
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    # Связь с автором
    author = relationship("Author", back_populates="posts")
    # Связь с комментариями
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


# Модель таблицы "comments"
class Comment(Base):
    __tablename__ = "comments"  # Имя таблицы

    id = Column(Integer, primary_key=True, index=True)  # Первичный ключ
    text = Column(Text, nullable=False)  # Текст комментария
    author_name = Column(String(100), nullable=False)  # Имя автора комментария
    created_at = Column(DateTime, default=datetime.utcnow)  # Дата создания
    # Внешний ключ: ссылается на id из таблицы posts
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    # Связь с постом
    post = relationship("Post", back_populates="comments")