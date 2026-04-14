from fastapi import FastAPI
from database.connection import Settings
from routes.events import router as event_router
from routes.users import router as user_router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    settings = Settings()
    await settings.initialize_database()


# routes
app.include_router(event_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "API is working 🚀"}