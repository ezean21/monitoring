FROM python:3.8.3-slim-buster

ADD py /root/py

WORKDIR /root/py

RUN mkdir -p /logs && chmod 775 /logs

RUN pip install -r requirements.txt

