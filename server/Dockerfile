# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app /app

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
