FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Since context is backend/, copy everything inside backend directly
COPY . .

RUN pip install -r requirements.txt

ENV SPCLASS_MODEL_URL="https://drive.google.com/uc?id=1SbogyD1-abBIZOqR5oiNjyojcRbHcsln"
ENV SPFAULT_MODEL_URL="https://drive.google.com/uc?id=1BFX7R7gYeNvXHcylOdRDdG6xXt3LMXvq"

RUN python api/models/startup.py

RUN ls -l
RUN ls -l api/



# Just download the model, do NOT load into memory
#RUN python api/models/startup.py

CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port $PORT"]
#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "10000"]
