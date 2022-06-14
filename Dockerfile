FROM python:3.9.5-slim-buster

WORKDIR /usr/src/warpoint

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile.lock Pipfile /usr/src/warpoint/
RUN pip install -U pip pipenv && pipenv install --system --deploy

COPY . .
