FROM python:3.10.6-alpine

RUN apk add --no-cache git gcc musl-dev
RUN git clone https://github.com/kljunowsky/XXElixir

WORKDIR /XXElixir

ENTRYPOINT ["python", "XXElixir.py"]
