# Use the official Python image from the Docker Hub as the base image
FROM python:3

# Set environment variable to ensure the Python output is sent straight to the terminal (e.g., for logging)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the Docker container to /app
WORKDIR /app

# Copy the requirements.txt file from the host to the current working directory in the container
COPY requirements.txt ./

# Upgrade pip to the latest version
RUN pip3 install --upgrade pip

# Install the dependencies specified in the requirements.txt file
RUN pip3 install -r requirements.txt

# Copy all the files from the host's current directory to the current working directory in the container
COPY . .

# Set the entrypoint for the container to execute the entrypoint.sh script using sh
ENTRYPOINT ["sh", "entrypoint.sh"]
