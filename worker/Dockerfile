FROM python:3.10-alpine

COPY . /worker


WORKDIR /worker 
RUN pip install -r requirements.txt 
RUN chmod 644 worker.py