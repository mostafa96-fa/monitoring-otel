# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /test

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN opentelemetry-bootstrap -a install


COPY . .

CMD ["python", "web.py"]