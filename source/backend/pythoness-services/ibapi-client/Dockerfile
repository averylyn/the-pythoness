FROM python:3.9-slim

WORKDIR /ibapi-client

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY source/backend/pythoness-services/ibapi-client/Client.py /ibapi-client/Client.py
COPY source/backend/pythoness-services/ibapi-client/Node.py /ibapi-client/Node.py
COPY source/backend/pythoness-services/ibapi-client/main.py /ibapi-client/main.py

CMD ["python", "-X", "frozen_modules=off", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "main.py"]
