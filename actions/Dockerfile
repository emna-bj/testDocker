FROM rasa/rasa-sdk:2.7.0

USER root

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

USER 1001
