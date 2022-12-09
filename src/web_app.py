import fastapi
from model import *
from Note import Note

api_router = fastapi.APIRouter()
notes_path = 'notes/'

@api_router.get('/{token}/note_info', response_model=NoteInfo)
def note_info(token, id: int):
    isntExist = Note.isntExist(id)
    if not Note.getTokenList().__contains__(str(token)) or isntExist:
        return NoteInfo(created_at=datetime(1, 1, 1), updated_at=datetime(1, 1, 1))
    else:
        note = Note(id)
        info = note.getNoteInfo()
        return NoteInfo(created_at=info[1], updated_at=info[2])

@api_router.get('/{token}/get_note_text', response_model=GetNoteText)
def get_note_text(token: str, id: int):
    isntExist = Note.isntExist(id)
    if not Note.getTokenList().__contains__(str(token)) or isntExist:
        return GetNoteText(id=-1,text='-1')
    else:
        note = Note(id)
        response = GetNoteText(
            id=id,
            text=note.text)
        return response

@api_router.post('/{token}/create_note', response_model=CreateNote)
def create_note(token: str, id: int):
    if not Note.getTokenList().__contains__(str(token)):
        return CreateNote(id=-1)
    else:
        note = Note(id)
        return CreateNote(id=note.id)

@api_router.patch('/{token}/edit_note', response_model=GetNoteText)
def edit_note(token: str, id: int, text: str):
    if not Note.getTokenList().__contains__(str(token)):
        return GetNoteText(id=-1, text='')
    else:
        note = Note(id)
        if text != '':
            note.editNote(text)
        return GetNoteText(id=note.id, text=note.text)

@api_router.get('/{token}/get_note_list', response_model=GetNoteList)
def get_note_list(token: str):
    if not Note.getTokenList().__contains__(str(token)):
        return GetNoteList(noteList=[])
    else:
        return GetNoteList(noteList=Note.getList())

@api_router.delete('/{token}/delete_note', response_model=CreateNote)
def delete_note(token: str, id: int):
    if not Note.getTokenList().__contains__(str(token)):
        return CreateNote(id=-1)
    else:
        note = Note(id)
        note.deleteNote()
        return CreateNote(id=id)
