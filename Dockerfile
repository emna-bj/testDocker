FROM rasa/rasa:2.7.1-full

# Use subdirectory as working directory
WORKDIR /app

USER root

COPY . /app
RUN ls -l

USER 1001
