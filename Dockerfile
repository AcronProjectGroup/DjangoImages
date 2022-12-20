FROM python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code


COPY requirements.txt /code/
RUN pip intall -r requirements.txt

COPY . /code/

