FROM python:3.11-slim

WORKDIR /app

# Устанавливаем uv и обновляем pip
RUN pip install --no-cache-dir -U pip uv

# Копируем только конфиги зависимостей
COPY pyproject.toml .
COPY uv.lock* .  

# Устанавливаем зависимости
RUN uv pip install --system --no-cache .

# Копируем код приложения
COPY . .

EXPOSE 8000

# Запуск FastAPI
CMD ["uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "8000"]
