# Базовый образ
FROM python:3.11-slim

# Установка зависимостей для PostgreSQL
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копирование и установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]