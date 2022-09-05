FROM python:3.8
LABEL maintainer="Derek Manning"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements /app/requirements
RUN pip install -r requirements/local.txt

COPY . .