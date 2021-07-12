FROM rasa/rasa:2.7.1-full

# Use subdirectory as working directory
WORKDIR /app

COPY requirements.txt ./

USER root

RUN pip install -r requirements.txt

COPY . /app
RUN ls -l

USER 1001
