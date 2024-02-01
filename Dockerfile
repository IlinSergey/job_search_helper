FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
