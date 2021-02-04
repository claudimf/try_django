FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /try_django
WORKDIR /try_django
ADD requirements.txt /try_django/
RUN pip install -r requirements.txt
RUN pip install django-extensions
ADD . /try_django/