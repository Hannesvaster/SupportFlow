from typing import Optional, List

from fastapi import APIRouter, Depends, Query
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


@router.get("", response_model=List[TicketOut])
def list_tickets(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    q = db.query(Ticket).filter(Ticket.owner_id == user.id)

    if status:
        q = q.filter(Ticket.status == status)

    if priority:
        q = q.filter(Ticket.priority == priority)

    tickets = (
        q.order_by(Ticket.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    return tickets
