# SupportFlow API (Commit 4)

SupportFlow is a backend API for managing support tickets with user authentication.  
This repo reflects the state up to **Commit 4**: DB + migrations + JWT auth + protected ticket creation.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Auth
- Docker Compose
- Pydantic v2

## Features
- `GET /health` (checks API + DB)
- `POST /auth/register`
- `POST /auth/login` (JWT)
- `POST /tickets` (protected)

## Getting Started

### 1) Run with Docker
```bash
docker compose up -d --build
