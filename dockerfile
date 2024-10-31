FROM python:3.10-slim

WORKDIR /home/clencyc/Dev/Fraud-Detection-Machine-Learning/Models

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD [ "python", "best_model_random_forest.pkl" ]
