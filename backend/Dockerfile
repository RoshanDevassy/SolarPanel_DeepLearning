FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Copy only backend folder (or entire repo if small)
COPY ./backend ./backend

WORKDIR /app/backend

RUN pip install -r api/requirements.txt

ENV SPCLASS_MODEL_URL="https://drive.google.com/uc?id=1SbogyD1-abBIZOqR5oiNjyojcRbHcsln"
ENV SPFAULT_MODEL_URL="https://drive.google.com/uc?id=1BFX7R7gYeNvXHcylOdRDdG6xXt3LMXvq"

# Run startup.py first to download models, then start server
CMD ["sh", "-c", "python api/models/startup.py && uvicorn api.main:app --host 0.0.0.0 --port 10000"]
