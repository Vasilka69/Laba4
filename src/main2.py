from model import *


if __name__ == '__main__':
    response1 = NoteInfo(created_at=datetime(2022,2,3), updated_at=datetime(2021,2,2))
    response2 = GetNoteText(id=2,text='TEXT')
    response3 = CreateNote(id=3)
    response4 = GetNoteList(noteInfo={0: 789, 1: 456, 2: 123})
    print(response1.json())
    print(response2.json())
    print(response3.json())
    print(response4.json())