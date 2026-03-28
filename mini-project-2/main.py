from fastapi import FastAPI
from database.connection import init_db
from routes.events import router as event_router

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(event_router)

@app.get("/")
async def root():
    return {"message": "API is working 🚀"}