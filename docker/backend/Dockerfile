FROM python:3.6
RUN apt-get update
RUN apt-get install -y gettext
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD tests/requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
ADD . /code/
