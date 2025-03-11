FROM python:latest

RUN pip install ibapi pandas numpy matplotlib

COPY IBClient.py /app/IBClient.py
COPY main.py /app/main.py

WORKDIR /app

CMD ["python", "main.py"]