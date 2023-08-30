# syntax=docker/dockerfile:1
FROM python:slim-buster

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

ENV CURRENT_ENVIRONMENT=PRODUCTION

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
