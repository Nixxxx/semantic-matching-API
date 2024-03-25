# base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# exposed port
EXPOSE 5000

# Start the Flask application
CMD ["flask", "--app", "semanticMatching", "run", "--host=0.0.0.0"]
