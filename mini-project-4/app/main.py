from fastapi import (
    FastAPI,
    HTTPException,
    WebSocket,
    WebSocketDisconnect,
    Request
)

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv

from app.models import PollCreate
from app.storage import polls
from app.websocket_manager import manager

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

poll_counter = 1


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )


@app.post("/polls")
def create_poll(poll: PollCreate):

    global poll_counter

    poll_data = {
        "id": poll_counter,
        "question": poll.question,
        "votes": {
            option: 0 for option in poll.options
        }
    }

    polls[poll_counter] = poll_data

    poll_counter += 1

    return poll_data


@app.get("/polls")
def get_polls():

    return list(polls.values())


@app.get("/polls/{poll_id}")
def get_poll(poll_id: int):

    if poll_id not in polls:

        raise HTTPException(
            status_code=404,
            detail="Poll not found"
        )

    return polls[poll_id]


@app.post("/polls/{poll_id}/vote")
async def vote_poll(
    poll_id: int,
    option: str
):

    if poll_id not in polls:

        raise HTTPException(
            status_code=404,
            detail="Poll not found"
        )

    if option not in polls[poll_id]["votes"]:

        raise HTTPException(
            status_code=400,
            detail="Invalid option"
        )

    polls[poll_id]["votes"][option] += 1

    await manager.broadcast(
        poll_id,
        {
            "type": "vote_update",
            "poll": polls[poll_id]
        }
    )

    return polls[poll_id]


@app.delete("/polls/{poll_id}")
def delete_poll(poll_id: int):

    if poll_id not in polls:

        raise HTTPException(
            status_code=404,
            detail="Poll not found"
        )

    deleted_poll = polls.pop(poll_id)

    return {
        "message": "Poll deleted",
        "poll": deleted_poll
    }


@app.websocket("/ws/polls/{poll_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    poll_id: int
):

    await manager.connect(
        poll_id,
        websocket
    )

    try:

        while True:

            data = await websocket.receive_json()

            option = data.get("option")

            if option in polls[poll_id]["votes"]:

                polls[poll_id]["votes"][option] += 1

                await manager.broadcast(
                    poll_id,
                    {
                        "type": "vote_update",
                        "poll": polls[poll_id]
                    }
                )

    except WebSocketDisconnect:

        manager.disconnect(
            poll_id,
            websocket
        )