
# Tasks API

FastAPI проект с тестами на pytest и возможностью запуска через Docker.

---

## Установка и запуск локально

1. Клонируем проект

2. Создаём виртуальное окружение и активируем его

3. Устанавливаем зависимости:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Запускаем сервер:

```bash
uvicorn app.main:app --reload
```

Теперь можно отправлять запросы на http://127.0.0.1:8000 через Postman (или как вам удобно).

Swagger UI доступен по пути http://127.0.0.1:8000/docs.

---

## Запуск тестов

1. Запускаем pytest из корня проекта:

```bash
pytest
```

- Тесты используют специальную SQLite базу (`test.db`), чтобы не трогать основную.

---

## Запуск через Docker (опционально)

1. Собираем и запускаем контейнер:

```bash
docker-compose up -d --build
```

2. Доступ к приложению:

- FastAPI: [http://localhost:8000](http://localhost:8000)  
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  

3. Для остановки:

```bash
docker-compose down
```

