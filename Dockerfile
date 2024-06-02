FROM python:3.11-slim-buster

WORKDIR /app

COPY api/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY api/ ./api

COPY model/model.pkl ./model/model.pkl
COPY model/scaler.pkl ./model/scaler.pkl

COPY initializer.sh ./initializer.sh

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT ["./initializer.sh"]