FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Copy dependency files first to leverage Docker cache
COPY ./requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy rest of the application
COPY . .

# Environment variables for model download
ENV SPCLASS_MODEL_URL="https://drive.google.com/uc?id=1SbogyD1-abBIZOqR5oiNjyojcRbHcsln"
ENV SPFAULT_MODEL_URL="https://drive.google.com/uc?id=1BFX7R7gYeNvXHcylOdRDdG6xXt3LMXvq"

# ✅ Download models during Docker build
RUN python api/models/startup.py

# Expose port
EXPOSE 10000

# ✅ Start app only (models already downloaded)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "10000"]
