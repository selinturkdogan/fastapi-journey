from fastapi import APIRouter
from models.events import Event

router = APIRouter()

@router.post("/events")
async def create_event(event: Event):
    await event.insert()
    return event