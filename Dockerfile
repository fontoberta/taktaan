FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
RUN mkdir /code
WORKDIR /code
ADD requirements.pip /code/
RUN pip3 install -r requirements.pip
ADD . /code/
ADD taktaan.ini /etc/uwsgi
ADD taktaan.service /etc/systemd/system
