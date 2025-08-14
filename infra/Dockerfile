FROM python:3.10.14

WORKDIR /app

COPY ../src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ../src /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]