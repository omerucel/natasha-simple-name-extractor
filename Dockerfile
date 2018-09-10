FROM python:3.7.0-alpine3.8
MAINTAINER Ömer ÜCEL <omerucel@gmail.com>
RUN pip install --no-cache-dir natasha
WORKDIR /data/project
COPY simple_name_extractor.py ./