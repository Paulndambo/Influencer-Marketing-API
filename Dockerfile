# syntax=docker/dockerfile:1
FROM python:slim-buster

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
