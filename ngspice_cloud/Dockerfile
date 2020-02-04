FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk add --no-cache --virtual .build-deps postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libpq5\
    && pip install --upgrade pip\
    && pip install --trusted-host pypi.python.org -r requirements.txt \
    && apk del .build-deps