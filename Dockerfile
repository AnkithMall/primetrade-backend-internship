# Use official Python base image with version 3.13.5
FROM python:3.13.5-slim

# Set working directory
WORKDIR /app

# Copy only necessary files from backend
COPY backend/requirements.txt .
COPY backend/app ./app
COPY backend/main.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
