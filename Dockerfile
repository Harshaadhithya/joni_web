FROM python:3.9

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/staticfiles
RUN mkdir -p /usr/src/app/media
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get -y install pdftk
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app