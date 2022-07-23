FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
COPY docker/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000