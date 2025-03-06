FROM python:latest

# Install the IB API
RUN pip install ibapi, pandas, numpy, matplotlib, sckit-learn, tensorflow, keras

# Copy the source code
COPY IBApi.py /app/IBApi.py
COPY main.py /app/main.py

# Set the working directory
WORKDIR /ib-api

# Run the application
CMD ["python", "main.py"]