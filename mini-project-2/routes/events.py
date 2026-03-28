from fastapi import APIRouter
from models.events import Event

router = APIRouter()

@router.post("/events")
async def create_event(event: Event):
    await event.insert()
    return event

@router.get("/events")
async def get_events():
    events = await Event.find().to_list()
    return events