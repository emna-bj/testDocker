FROM rasa/rasa-sdk:2.7.0

USER root

WORKDIR /app

COPY actions/actions.py /app/actions
COPY actions /app/actions
RUN ls -l

USER 1001

CMD ["start","--actions", "actions.actions"]
