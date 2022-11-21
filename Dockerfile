FROM python:3.8

WORKDIR Uses/anon/Projects/app

COPY . .

RUN pip install -r requirements.txt


