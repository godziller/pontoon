# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application files into the container
COPY *.py .

# Specify the command to run the application (adjust based on your project)
CMD ["python", "./PontoonGame.py"]
