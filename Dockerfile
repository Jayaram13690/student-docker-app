# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Run python file
CMD ["python", "app.py"]