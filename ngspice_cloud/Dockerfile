FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code
RUN apk add postgresql-dev
COPY requirements.txt /code/
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev\
    && pip install --upgrade pip\
    && pip install --trusted-host pypi.python.org -r requirements.txt \
    && apk del .build-deps