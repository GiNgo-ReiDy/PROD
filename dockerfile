FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости
COPY pyproject.toml uv.lock ./

# Устанавливаем uv (если используется) или pip
RUN pip install --no-cache-dir -e .

# Копируем весь проект
COPY . .

# Копируем бэкенд и фронтенд
COPY back/ ./back/
COPY front/ ./front/

# Открываем порт
EXPOSE 80

# Команда запуска (адаптируйте под ваш проект)
CMD ["uvicorn", ".main:app", "--host", "0.0.0.0", "--port", "80"]