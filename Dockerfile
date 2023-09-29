FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential
RUN pip install pipenv
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY web .

CMD python app.py
