FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++ git wget curl && \
    pip install --upgrade pip

# Since context is backend/, copy everything inside backend directly
COPY . .

RUN pip install -r requirements.txt

RUN python api/models/startup.py

RUN ls -l
RUN ls -l api/



# Just download the model, do NOT load into memory
#RUN python api/models/startup.py
CMD exec uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8080}
#CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port $PORT"]
#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "10000"]
