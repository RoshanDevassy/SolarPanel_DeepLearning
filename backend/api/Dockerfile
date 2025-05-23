FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Copy necessary files
COPY ./models ./models
COPY ./main.py ./main.py
COPY ../requirements.txt ./requirements.txt

# Install Python packages
RUN pip install -r requirements.txt

# Set environment variables for downloading models (if needed in startup.py)
ENV SPCLASS_MODEL_URL="https://drive.google.com/uc?id=1SbogyD1-abBIZOqR5oiNjyojcRbHcsln"
ENV SPFAULT_MODEL_URL="https://drive.google.com/uc?id=1BFX7R7gYeNvXHcylOdRDdG6xXt3LMXvq"

# Run startup and launch app
CMD ["sh", "-c", "python models/startup.py && uvicorn main:app --host 0.0.0.0 --port 10000"]
