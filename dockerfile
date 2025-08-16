# Use a Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the entire application code first
# This ensures that all files (including the one needed for '-e .')
# are available during the pip install step.
COPY . .

# Install dependencies from the requirements file
# The '-e .' dependency will now work correctly.
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Command to run the application
# Assumes your main FastAPI app instance is named 'app'
# and is located in 'main.py'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
