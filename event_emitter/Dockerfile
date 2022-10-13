### 1. Get python image
FROM python:3.7-buster

RUN apt-get update -y && \
    apt-get upgrade -y


### 2. Install Python
COPY requirements.txt /src/
WORKDIR /src


RUN pip install -r requirements.txt

COPY client.py /src/



