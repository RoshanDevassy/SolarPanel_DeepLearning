FROM python:3.10-slim

WORKDIR /app

# Install basic tools and upgrade pip
RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Copy entire backend contents into the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Set environment variables for model download (optional if using startup script)
ENV SPCLASS_MODEL_URL="https://drive.google.com/uc?id=1SbogyD1-abBIZOqR5oiNjyojcRbHcsln"
ENV SPFAULT_MODEL_URL="https://drive.google.com/uc?id=1BFX7R7gYeNvXHcylOdRDdG6xXt3LMXvq"

# Run model download script (optional) and start the FastAPI app
CMD ["sh", "-c", "python models/startup.py && uvicorn main:app --host 0.0.0.0 --port 10000"]
