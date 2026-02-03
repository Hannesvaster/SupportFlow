from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.db import get_db
from app.models import Ticket
from app.schemas import TicketOut
from app.security import get_current_user
from app.models import User

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("/", response_model=List[TicketOut])
def get_tickets(
    status: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    limit: int = Query(10, ge=1, le=50),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Ticket).filter(Ticket.owner_id == current_user.id)

    if status:
        query = query.filter(Ticket.status == status)

    if priority:
        query = query.filter(Ticket.priority == priority)

    tickets = query.offset(offset).limit(limit).all()
    return tickets
