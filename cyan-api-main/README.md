# cyan-api

## Описание
Проект для вывода собранных данных

## Структура проекта

- `repo/` — репозитории
- `db/` — модуль работы с бд
- `core/` — конфиг
- `api/` — роутеры

## Установка

```bash

cd cyan-api
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Настройка

1. Пререместить базу в папку 'db'
2. В файле `app/core/config.py` укажите переменную DB_PATH

## Работа программы
Запуск api — ```bash uvicorn app.main:app --reload```