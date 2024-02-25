# Snag that shiny Python 3.12-slim image from DockerHub
FROM python:3.12-slim

WORKDIR /app

COPY ../setup.py /app
COPY ../chatroom_simulator /app/chatroom_simulator

RUN pip install --no-cache-dir . && \
    useradd -m appuser && \
    chown -R appuser:appuser /app

USER appuser

ENTRYPOINT [ "chatroom-simulator" ]