FROM python:3.10.7-slim-buster

WORKDIR /usr/src/app


RUN pip install --upgrade pip
COPY ./project/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/