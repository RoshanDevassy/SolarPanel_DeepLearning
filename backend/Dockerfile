FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

RUN python api/models/startup.py

RUN ls -l
RUN ls -l api/

CMD exec uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8080}
