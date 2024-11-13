FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt requirements.txt

COPY /Models/best_model_random_forest.pkl best_model_random_forest.pkl
COPY main.py main.py

RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "main.py" ]
