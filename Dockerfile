# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask pymysql

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]

