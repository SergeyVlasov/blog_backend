# 📝 Blog API (Django + Django Ninja)

REST API для блога, построенный на Django и Django Ninja с PostgreSQL и Docker.

---

## 🚀 Возможности

- Регистрация и аутентификация через Bearer Token  
- CRUD для постов  
- Категории постов  
- Комментарии к постам  
- Авторизация на уровне объектов (owner-only)  
- Swagger-документация (OpenAPI)  
- Админ-панель Django  
- Логирование действий пользователей  

---

## 🧱 Стек технологий

- Python 3.12  
- Django 4.2  
- Django Ninja 1.2.2  
- PostgreSQL 15  
- Docker / Docker Compose  
- Pytest + pytest-django  

---

## 📦 Быстрый старт

### Клонировать проект

```bash
git clone <repo-url>
cd blog_backend
```

### Запуск через Docker

```bash
docker compose up --build
```

API будет доступен:

http://localhost:8000

---

## 📚 API документация

Swagger UI:

http://localhost:8000/api/docs

OpenAPI schema:

http://localhost:8000/api/openapi.json

---

## 🔐 Аутентификация

Используется Bearer Token.

Пример заголовка:

Authorization: Bearer <token>

---

## 📌 Основные эндпоинты

### 👤 Users
- POST /api/users/register — регистрация  
- POST /api/users/login — логин  

### 📝 Posts
- GET /api/posts/ — список постов  
- POST /api/posts/ — создать пост (auth)  
- PUT /api/posts/{id} — обновить пост (owner)  
- DELETE /api/posts/{id} — удалить пост (owner)  

### 💬 Comments
- GET /api/comments/ — список комментариев  
- POST /api/comments/ — создать комментарий (auth)  
- PUT /api/comments/{id} — обновить (owner)  
- DELETE /api/comments/{id} — удалить (owner)  

### 🏷 Categories
- GET /api/categories/  
- POST /api/categories/ (auth)  
- DELETE /api/categories/{id} (auth)  

---

## 🧪 Тестирование

### Запуск всех тестов

```bash
docker compose run --rm web pytest -v
```

### Запуск в уже поднятом контейнере

```bash
docker compose exec web pytest -v
```

---

## 🐳 Docker

Сервисы:
- web — Django API  
- db — PostgreSQL 15  

---

## ⚙️ Переменные окружения

| Variable     | Default   |
|--------------|----------|
| DB_NAME      | blog      |
| DB_USER      | postgres  |
| DB_PASSWORD  | postgres  |
| DB_HOST      | db        |
| DB_PORT      | 5432      |

---

## 🗂 Архитектура проекта

```
apps/
 ├── users
 ├── posts
 ├── comments
 ├── categories

core/
 ├── auth.py
 ├── permissions.py
 ├── logging.py

config/
 ├── settings.py
 ├── urls.py
```

---

## 📊 Логирование

Логи пишутся в:

app.log

Также выводятся в консоль Docker.

---

## 🧠 Особенности реализации

- Custom User Model (AbstractUser)  
- Token-based auth через HttpBearer  
- Owner-based access control  
- Router-based API (Django Ninja)  
- PostgreSQL через Docker  

---

## 📦 Production improvements (future)

- Redis caching  
- Celery background tasks  
- JWT refresh tokens  
- Rate limiting  
- CI/CD (GitHub Actions)  
- Nginx reverse proxy  

---

## 📜 Лицензия

MIT