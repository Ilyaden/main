# Установка базового образа
FROM python:3.10.0

# Установка переменной окружения для запуска в режиме production
ENV DJANGO_ENV=production

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование файла зависимостей в контейнер
COPY requirements.txt .

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование исходного кода приложения в контейнер
COPY . .

# Запуск команды для запуска Django-приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]