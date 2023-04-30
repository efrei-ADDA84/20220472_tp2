FROM python:3.9-alpine

WORKDIR /app

COPY TP01DEVOPS.py /app/
COPY TP02DEVOPS.py /app/

RUN pip install flask requests

EXPOSE 5000

CMD ["python", "TP2.py"]

