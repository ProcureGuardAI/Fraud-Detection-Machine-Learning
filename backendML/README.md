# Fraud Detection Machine Learning Backend

This project is a backend service for a fraud detection machine learning application. It is built using Django and Django REST framework, and it uses Docker for containerization.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Transaction management
- Notification system
- Reporting system
- RESTful API endpoints
- Dockerized for easy deployment

## Requirements

- Python 3.10+
- Docker
- Docker Compose

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/fraud-detection-backend.git
   cd fraud-detection-backend

2. **create and activate a virtual environment:**

    ```sh
    python -m venv myenv
    source myenv/bin/activate 

3. **Install the dependencies**

    ```sh
    pip install -r requirements.txt

4. **Set up environment variables:**

    ```sh 
    SECRET_KEY='your-secret-key'
    DEBUG=True
    DJANGO_ALLOWED_HOSTS=*,localhost,127.0.0.1,[::1]
    DATABASE_URL=postgres://myuser:mypassword@db:5432/mydatabase

5. **Run database migrations:**

    ```sh
    python manage.py migrate

6. **Create superuser**

    ```sh
    python manage.py createsuperuser

### Usage
1. **Run the development server**

    ```sh
    python manage.py runserver

2. **Access the application:**
   Open your browser and go to http://localhost:8000.

### API EndPoints
#### User Registration

1. Endpoint /api/users/register/
2. Method: POST
3. Payload

    ```sh
    {
    "full_name": "Bobby Stearman",
    "email": "bobby@didcoding.com",
    "phone_number": "1234567890",
    "password1": "SecurePassword123",
    "password2": "SecurePassword123",
    "role": "Developer",
    "department": "Procurement",
    "office_location": "Headquarters",
    "security_question": "What is your first pet's name?",
    "two_fa": true
    }


#### Transactions
- Endpoint: /api/transactions/
- Method: GET, POST

#### Notifications
- Endpoint: /api/notifications/
- Method: GET, POST

#### Reports
- Endpoint: /api/reports/
- Method: GET, POST

## Docker
1. Build and start the containers:

    ```sh
    sudo docker-compose up -d --build

2. Check running containers:

    ```sh
    docker ps

3. view logs

    ```sh
    docker-compose logs

4. Stop containers

    ```sh
    sudo docker-compose down

