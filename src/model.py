import json
from datetime import datetime
from pydantic import BaseModel
from typing import Dict

class NoteInfo(BaseModel):
    created_at: datetime
    updated_at: datetime

class GetNoteText(BaseModel):
    id: int
    text: str

class CreateNote(BaseModel):
    id: int

class GetNoteList(BaseModel):
    notesList: Dict[int, int]
