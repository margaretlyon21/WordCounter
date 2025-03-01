 # Use a lightweight base image with Python installed
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home

# Copy the Python script and the data directory into the container
COPY home/countwords.py /home/countwords.py
COPY home/data /home/data

# Install any necessary dependencies (if required)
RUN pip install --no-cache-dir --upgrade pip

# Set the default command to run the script
CMD ["python", "countwords.py"]

