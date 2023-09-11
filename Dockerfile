FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY run_task.sh run_task.sh

RUN chmod +x run_task.sh

RUN apt-get update && apt-get -y install cron

COPY present-cron /etc/cron.d/main-cron

RUN chmod 0644 /etc/cron.d/main-cron

RUN crontab /etc/cron.d/main-cron

COPY task.py task.py

CMD ["sh", "-c", "echo 'Presentation cron starting...'; /code/run_task.sh && cron -f"]