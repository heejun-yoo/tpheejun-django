FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /web
COPY . .
RUN pip install --upgrade pip
RUN pip install Django psycopg2 djangorestframework requests gunicorn whitenoise ipdb