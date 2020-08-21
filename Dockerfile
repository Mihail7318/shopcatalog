# pull official base image
FROM python:3.6
MAINTAINER Nickolay Kuzmin <kng197@mail.ru>


# set work directory
WORKDIR /shopcatalog/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .