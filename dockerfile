FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости
COPY pyproject.toml uv.lock ./

# Устанавливаем uv (если используется) или pip
RUN pip install --no-cache-dir -e .

# Копируем весь проект
COPY . .

COPY back /app/back
COPY front/dist /app/front/dist  

EXPOSE 80

CMD ["uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "80"]