FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

CMD ["python", "./app.py"]