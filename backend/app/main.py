from fastapi import FastAPI
from app.db import check_db_connection

app = FastAPI(title="SupportFlow API")

@app.get("/health")
def health():
    db_ok = check_db_connection()
    return {"status": "ok", "db": "ok" if db_ok else "down"}
