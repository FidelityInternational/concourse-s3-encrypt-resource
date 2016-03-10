FROM python:3.5-alpine

# https://github.com/yikaus/docker-alpine-bash/blob/34b9807/Dockerfile#L4
RUN apk add --update bash

RUN pip install --upgrade pip
RUN pip install --upgrade awscli

ADD assets/ /opt/resource/
# RUN chmod a+x

CMD echo Simple S3 Resource ready.
