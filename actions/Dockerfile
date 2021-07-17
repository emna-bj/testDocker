FROM rasa/rasa-sdk:2.7.0

USER root

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN ls -l

USER 1001

CMD ["start","--actions", "actions.actions"]
