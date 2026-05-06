from pydantic import BaseModel
from typing import Dict


class PollCreate(BaseModel):
    question: str
    options: list[str]


class Poll(BaseModel):
    id: int
    question: str
    votes: Dict[str, int]