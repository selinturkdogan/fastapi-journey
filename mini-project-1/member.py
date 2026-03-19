from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import Member
import asyncio

member_router = APIRouter()

# Template engine
templates = Jinja2Templates(directory="templates")

# Mock database
members = []

# API ENDPOINTS 

@member_router.get("/members/")
async def get_members():
    await asyncio.sleep(1)
    return members

@member_router.get("/members/{member_id}")
async def get_member(member_id: int):
    for member in members:
        if member.id == member_id:
            return member

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found"
    )

@member_router.post("/members/")
async def add_member(member: Member):
    members.append(member)
    return member

@member_router.put("/members/{member_id}")
async def update_member(member_id: int, updated_member: Member):
    for index, member in enumerate(members):
        if member.id == member_id:
            members[index] = updated_member
            return updated_member

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found"
    )

@member_router.delete("/members/{member_id}")
async def delete_member(member_id: int):
    for member in members:
        if member.id == member_id:
            members.remove(member)
            return {"message": "Member deleted"}

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found")


# ─HTML ROUTES (JINJA2) ─

@member_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "members": members
    })


@member_router.get("/member/{id}", response_class=HTMLResponse)
async def get_member_page(request: Request, id: int):
    for member in members:
        if member.id == id:
            return templates.TemplateResponse("member.html", {
                "request": request,
                "member": member
            })

    raise HTTPException(status_code=404, detail="Member not found")