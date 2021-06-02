FROM python:3.9.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY req.txt /code/

RUN pip install -r req.txt
COPY . /code/


CMD python redisMonitor.py
