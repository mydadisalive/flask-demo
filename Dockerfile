# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files into the container
COPY app.py .
COPY templates templates
COPY static static

# Expose the port that Flask app runs on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
