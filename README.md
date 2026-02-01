# SupportFlow

SupportFlow is an internal ticket & workflow management system.

▶️ Getting Started
1. Clone repository
git clone https://github.com/yourusername/SupportFlow.git
cd SupportFlow

2. Start services
docker compose up -d --build


API will be available at:

http://localhost:8000


Swagger UI:

http://localhost:8000/docs

🔍 Health Check
GET /health


Response:

{
  "status": "ok",
  "db": "ok"
}

🔐 Authentication
Register user
POST /auth/register
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "secret123"
}


Response:

{
  "id": 1,
  "email": "test@example.com"
}

Login
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=test@example.com
password=secret123


Response:

{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}

🎫 Create Ticket (Protected Endpoint)
POST /tickets
Authorization: Bearer JWT_TOKEN
Content-Type: application/json

{
  "title": "My first ticket",
  "description": "Example issue",
  "priority": "high"
}


Response:

{
  "id": 1,
  "title": "My first ticket",
  "description": "Example issue",
  "status": "open",
  "priority": "high",
  "owner_id": 1
}

🧪 Database Migrations

Generate migration:

docker compose run --rm api alembic revision --autogenerate -m "message"


Apply migrations:

docker compose run --rm api alembic upgrade head
