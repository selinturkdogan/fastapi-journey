from fastapi import APIRouter
from models.events import Event
from fastapi import HTTPException

router = APIRouter()

@router.post("/events")
async def create_event(event: Event):
    await event.insert()
    return event

@router.get("/events")
async def get_events():
    events = await Event.find().to_list()
    return events

@router.get("/events/{event_id}")
async def get_event(event_id: str):
    event = await Event.get(event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event

@router.delete("/events/{event_id}")
async def delete_event(event_id: str):
    event = await Event.get(event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    await event.delete()

    return {"message": "Event deleted successfully"}

@router.put("/events/{event_id}")
async def update_event(event_id: str, updated_event: Event):
    event = await Event.get(event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    event.title = updated_event.title
    event.image = updated_event.image
    event.description = updated_event.description
    event.tags = updated_event.tags
    event.location = updated_event.location

    await event.save()

    return event