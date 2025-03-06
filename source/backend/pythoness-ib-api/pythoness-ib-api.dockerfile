FROM python:latest

# Install the IB API
RUN pip install ibapi, pandas, numpy, matplotlib, sckit-learn, tensorflow, keras

# Copy the source code
COPY ib-api /ib-api

# Set the working directory
WORKDIR /ib-api

# Run the application
CMD ["python", "main.py"]