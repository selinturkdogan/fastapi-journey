from fastapi import FastAPI
from models import Member
import asyncio

app = FastAPI()

members = []

@app.get("/members/")
async def get_members():
    await asyncio.sleep(1)
    return members

@app.get("/members/{member_id}")
async def get_member(member_id: int):

    for member in members:
        if member.id == member_id:
            return member

    return {"error": "Member not found"}

@app.post("/members/")
async def add_member(member: Member):

    members.append(member)

    return member

@app.put("/members/{member_id}")
async def update_member(member_id: int, updated_member: Member):

    for index, member in enumerate(members):
        if member.id == member_id:
            members[index] = updated_member
            return updated_member

    return {"error": "Member not found"}

@app.delete("/members/{member_id}")
async def delete_member(member_id: int):

    for member in members:
        if member.id == member_id:
            members.remove(member)
            return {"message": "Member deleted"}

    return {"error": "Member not found"}