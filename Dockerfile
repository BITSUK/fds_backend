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
RUN pip install ez_setup
COPY ./requirements.txt /fds/app
RUN pip install -r requirements.txt

# copy project
COPY . /fds/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
