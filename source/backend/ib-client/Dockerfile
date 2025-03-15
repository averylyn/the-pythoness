FROM python:latest

RUN pip install ibapi pandas numpy matplotlib

RUN echo /run/secrets/tws_password

COPY IBClient.py /app/IBClient.py
COPY main.py /app/main.py

WORKDIR /app

CMD ["python", "main.py"]