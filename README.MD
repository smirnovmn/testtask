# TestTask

Тестовое задание CodesCommanders

## Структура проекта

- `app/api/user_router.py` — маршруты для пользователей  
- `app/api/order_router.py` — маршруты для заказов  
- `app/main.py` — основной файл приложения с объединёнными роутерами  

## Установка

1. Клонируйте репозиторий:

```bash
git https://github.com/smirnovmn/testtask
```

2. Установите виртуальное окружение 

```bash
python -m venv venv
source venv/bin/activate
```

2. Установите зависимости 

```bash
pip install -r requirements.txt
```

## Запуск 

Запуск через основной файл приложения:

```bash
uvicorn app.main:app --reload
```

Приложение будет доступно по адресу:
http://127.0.0.1:8000

Swagger UI для тестирования эндпоинтов:
http://127.0.0.1:8000/docs

Redoc документация:
http://127.0.0.1:8000/redoc

