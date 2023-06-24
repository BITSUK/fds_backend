# pull the official base image
#FROM python:3.11.3-alpine
FROM python:3.8.3-alpine

# set work directory
WORKDIR /fds/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
#RUN pip install ez_setup
RUN pip install django==4.2.1
RUN pip install djangorestframework==3.14.0
RUN pip install django-cors-headers==4.1.0
RUN apt-get update
RUN apt-get install libpq-dev python-dev-is-python3
RUN pip install drf-yasg
RUN pip install psycopg2==2.9.6
#RUN pip install -U drf-yasg
#RUN pip install coreapi pyyaml
#COPY ./requirements.txt /fds/app
#RUN pip install -r requirements.txt

# copy project
COPY . /fds/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
