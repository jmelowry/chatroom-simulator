FROM python:3.12-slim
WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir . \
    && useradd -m appuser \
    && chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["chatroom-simulator"]
