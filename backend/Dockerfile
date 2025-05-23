FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Since context is backend/, copy everything inside backend directly
COPY . .

RUN pip install -r requirements.txt

RUN ls -l
RUN ls -l api/


ENV SPCLASS_MODEL_URL="https://drive.google.com/uc?id=1SbogyD1-abBIZOqR5oiNjyojcRbHcsln"
ENV SPFAULT_MODEL_URL="https://drive.google.com/uc?id=1BFX7R7gYeNvXHcylOdRDdG6xXt3LMXvq"

CMD ["sh", "-c", "python api/models/startup.py && uvicorn api.main:app --host 0.0.0.0 --port 10000"]
