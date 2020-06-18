FROM python:3.8-alpine

RUN apk add --no-cache --update jq gnupg && \
    pip install --upgrade pip && \
    pip install --upgrade awscli

ADD assets/ /opt/resource/
