# 📝 FastAPI Message Board

Веб-приложение для управления сообщениями, построенное на современном фреймворке FastAPI. Приложение предоставляет как REST API, так и удобный веб-интерфейс.

## ✨ Особенности

- **REST API** - полный CRUD для работы с сообщениями
- **Веб-интерфейс** - UI-интерфейс для управления сообщениями
- **Документация API** - автоматически генерируемая документация Swagger/OpenAPI
- **Валидация данных** - строгая типизация с помощью Pydantic
- **Шаблонизация** - HTML страницы с Jinja2

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.10+
- pip (менеджер пакетов Python)

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kate-belova/messages_app.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd messages_app
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите приложение:
   ```bash
   python main.py
   ```
Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

📚 **Структура проекта**
```bash
fastapi-message-board/
├── main.py              # Основной файл приложения
├── api.py               # API эндпоинты
├── web.py               # Веб-эндпоинты
├── schemas.py           # Pydantic схемы
├── handlers/
│   └── routers.py       # Импорт роутеров
├── templates/           # HTML шаблоны
│   ├── index.html       # Главная страница
│   ├── create.html      # Страница создания сообщения
│   └── detail.html      # Страница деталей сообщения
├── static/              # Статические файлы (CSS, JS, изображения)
└── requirements.txt     # Зависимости проекта
```

## 🌐 Доступные интерфейсы:

### 🖥️ Веб-интерфейс
- **Главная страница:** [http://localhost:8000/web/messages](http://localhost:8000/web/messages)  
- **Создание сообщения:** [http://localhost:8000/web/messages/create](http://localhost:8000/web/messages/create)  
- **Детали сообщения:** [http://localhost:8000/web/messages/{id}](http://localhost:8000/web/messages/{id})

### 📘 API Документация
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)  
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧩 API Эндпоинты:

### 📝 Сообщения
```bash
| Метод    | URL                 | Описание                       |
|:--------:|:--------------------|:-------------------------------|
| `GET`    | `/messages`         | Получить все сообщения         |
| `GET`    | `/messages/{id}`    | Получить сообщение по ID       |
| `POST`   | `/messages`         | Создать новое сообщение        |
| `PUT`    | `/messages/{id}`    | Обновить сообщение             |
| `DELETE` | `/messages/{id}`    | Удалить сообщение по ID        |
| `DELETE` | `/messages`         | Удалить все сообщения          |
```
## 🛠 Технологии

- **FastAPI** — современный, быстрый веб-фреймворк  
- **Uvicorn** — ASGI-сервер  
- **Pydantic** — валидация данных и сериализация  
- **Jinja2** — шаблонизация HTML  
- **Starlette** — инструменты для веб (статические файлы, шаблоны)
