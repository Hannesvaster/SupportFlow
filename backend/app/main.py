from fastapi import FastAPI
from app.db import check_db_connection
from app.routers.auth import router as auth_router
from app.routers.tickets import router as tickets_router

app = FastAPI(title="SupportFlow API")

app.include_router(auth_router)
app.include_router(tickets_router)

@app.get("/health")
def health():
    db_ok = check_db_connection()
    return {"status": "ok", "db": "ok" if db_ok else "down"}
