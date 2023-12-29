FROM python:3.11

WORKDIR /app

ENV WATCHFILES_FORCE_POLLING=true

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
