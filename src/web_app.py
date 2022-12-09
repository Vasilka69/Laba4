import fastapi
from model import *
from Note import Note
#from main import *

tags_metadata = [
    {
        "name": "id"
    }
]

api_router = fastapi.APIRouter()
notes_path = 'notes/'

@api_router.get('/note_info', response_model=NoteInfo)
def note_info():
    return NoteInfo(created_at=datetime(2022,2,3), updated_at=datetime(2021,2,2))

@api_router.get('/get_note_text/id={id}', response_model=GetNoteText)
def get_note_text(id):
    filename = 'note' + str(id) + '.txt'
    path = notes_path + filename
    with open(path,'r') as f:
        response = GetNoteText(
            id=id,
            text=f.read())
    return response
#patch
@api_router.get('/create_note', response_model=CreateNote,)
def create_note(id: int):
    note = Note(id)
    return CreateNote(id=note.id)

#patch
@api_router.get('/edit_note', response_model=GetNoteText,)
def edit_note(id: int, text: str):
    note = Note(id)
    if text != '':
        note.editNote(text)
    return GetNoteText(id=note.id, text=note.text)

@api_router.get('/get_note_list', response_model=GetNoteList)
def get_note_list():
    return GetNoteList(noteInfo={0: 789, 1: 456, 2: 123})
