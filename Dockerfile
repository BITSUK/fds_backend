# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /fds/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /fds/app
#RUN pip install -r requirements.txt
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install psycopg2
RUN pip install -U drf-yasg
RUN pip install coreapi pyyaml

# copy project
COPY . /fds/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
