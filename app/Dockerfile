FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install flask psycopg2-binary

CMD ["python", "main.py"]
