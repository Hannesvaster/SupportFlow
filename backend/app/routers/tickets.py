from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Ticket
from app.schemas import TicketCreate, TicketOut
from app.auth import get_current_user

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.post("", response_model=TicketOut, status_code=201)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ticket = Ticket(
        title=payload.title,
        description=payload.description,
        priority=payload.priority,
        status="open",
        owner_id=user.id,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
