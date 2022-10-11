FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /web
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#CMD python manage.py runserver 0.0.0.0:$PORT