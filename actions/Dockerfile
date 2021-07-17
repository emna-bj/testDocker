FROM rasa/rasa-sdk:2.7.0

USER root

WORKDIR /app

COPY actions/actions.py /app
COPY actions/test.json /app
COPY actions/slots.json /app
COPY actions/requirements.txt /app

RUN ls -l

RUN pip install -r requirements.txt
ENTRYPOINT ["test.sh"]
USER 1001

CMD ["start","--actions", "actions.actions"]
