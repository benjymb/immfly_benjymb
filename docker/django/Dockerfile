FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /

COPY /app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY /app/wait-for-it.sh /app/wait-for-it.sh 
COPY /app/entrypoint.sh /app/entrypoint.sh

COPY app /app

EXPOSE 8000

WORKDIR /app

RUN chmod +x wait-for-it.sh
RUN chmod +x entrypoint.sh

CMD ["./wait-for-it.sh", "-t", "0", "db:5432", "--", "./entrypoint.sh"]
