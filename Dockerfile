# Description: Dockerfile based on Python 3.9.2 image to an FastAPI application
# Author: Sebastián Gámez Ariza

# Base image
FROM python:3.11.2

# Create the working directory
RUN mkdir /home/app

# Copy the requirements file
COPY requirements.txt /home/app

# Install the requirements
RUN pip install --no-cache-dir --upgrade -r /home/app/requirements.txt

# Set the working directory
WORKDIR /home/app

# Expose the port
EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]