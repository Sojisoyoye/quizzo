FROM python:3.6.8-alpine

LABEL quizzo app

WORKDIR /quizzo/server/src

COPY . .

RUN ["pip3", "install", "pipenv"]

RUN ["pipenv", "install"]

CMD pipenv run python main.py