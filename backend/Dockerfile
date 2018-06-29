FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn mydjango.wsgi -b 0.0.0.0:8000 & celery worker --app=myapp.tasks