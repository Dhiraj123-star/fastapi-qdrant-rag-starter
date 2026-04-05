# Use official Python Image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# RUN Fastapi
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]