FROM python:3.10-slim

WORKDIR /app

# Install basic tools and gdown
RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Copy only what's needed
COPY ./api ./api
COPY ./models/startup.py ./models/startup.py
COPY requirements.txt .

RUN pip install -r requirements.txt

# Set environment variables for model URLs
ENV SPCLASS_MODEL_URL="https://drive.google.com/uc?id=1SbogyD1-abBIZOqR5oiNjyojcRbHcsln"
ENV SPFAULT_MODEL_URL="https://drive.google.com/uc?id=1BFX7R7gYeNvXHcylOdRDdG6xXt3LMXvq"

# Use dynamic PORT for Render compatibility
CMD ["sh", "-c", "python models/startup.py && uvicorn api.main:app --host 0.0.0.0 --port $PORT"]
