FROM python:3.10-slim

WORKDIR /app

COPY ping.py .

EXPOSE 8085

CMD ["python", "ping.py"]

