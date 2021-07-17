FROM rasa/rasa-sdk:2.7.0

USER root

WORKDIR /app

COPY actions.py /app

COPY requirements.txt /app

RUN ls -l

RUN pip install -r requirements.txt

USER 1001

CMD ["start","--actions", "actions.actions"]
