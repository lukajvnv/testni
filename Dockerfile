FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN pip install --upgrade pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p myapp
COPY ./myapp ./myapp

RUN mkdir -p myapp/logs

EXPOSE 5000
CMD ["python", "myapp/app.py"]