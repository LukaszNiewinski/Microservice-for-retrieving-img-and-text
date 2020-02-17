FROM python:3.7.6-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .


CMD [ "python", "api.py" ]
