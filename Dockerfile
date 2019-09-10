FROM python:3.7-slim
MAINTAINER Daniel Arevalo
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir app
RUN pip install --upgrade pip
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt