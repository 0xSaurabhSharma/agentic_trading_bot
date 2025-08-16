# Use a Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the entire application code first
COPY . .

# Install dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Cloud Run will automatically set the PORT env variable.
# Expose the port (e.g., 8080) that the container will listen on.
EXPOSE 8080

# Command to run the application
# Use the $PORT environment variable to listen on the correct port.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
