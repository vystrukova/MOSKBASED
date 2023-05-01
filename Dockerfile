# указываем базовый образ
FROM python:3.9

# устанавливаем рабочую директорию
WORKDIR /api

# копируем файл с зависимостями
COPY requirements.txt .

# устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install bs4

# копируем код проекта в контейнер
COPY ../api .
COPY pytest.ini /api

# указываем переменную окружения PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/api"

# указываем команду для запуска тестов
CMD ["pytest"]

