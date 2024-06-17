# Используем официальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости для выполнения команд
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app 
RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]