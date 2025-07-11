# Dockerfile
FROM python:3.11-slim

# System dependencies
RUN apt-get update && apt-get install -y git build-essential && apt-get clean

# Copy files
WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port
ENV PORT=8000
EXPOSE 8000

# Run server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
