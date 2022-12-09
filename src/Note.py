from datetime import datetime
from typing import List
import Note

class Note:
    notes_path = 'notes/'
    notesInfo = notes_path + 'NotesInfo.txt'
    id: int
    text: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, id: int):
        self.id = id
        self.text = self.openFile()
        self.writeFile()

    def openFile(self):
        text = ''
        try:
            f = open(self.notes_path + str(self.id) + '.txt')
            text = f.read()
            info, i = self.checkInfo()
            if i != -1:
                self.updated_at = i[2]
                self.created_at = i[1]
            f.close()
        except FileNotFoundError:
            f = open(self.notes_path + str(self.id) + '.txt', 'w')
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.saveInfo()
            f.close()
        return text

    def writeFile(self):
        with open(self.notes_path + str(self.id) + '.txt', 'w') as f:
            f.write(self.text)
        self.saveInfo()

    def editNote(self, text: str):
        self.text = text
        self.updated_at = datetime.now()
        self.writeFile()

    def saveInfo(self):
        info, i = self.checkInfo()
        with open(self.notesInfo, 'w') as f:
            if i != -1:
                i[2] = self.updated_at
            if len(info) != 0:
                for j in info:
                    f.write(f'{j[0]},{j[1]},{j[2]}\n')
            else:
                f.write(f'{self.id},{self.created_at},{self.updated_at}\n')

    def checkInfo(self):
        try:
            open(self.notesInfo, 'r').close()
        except FileNotFoundError:
            return [], -1
        with open(self.notesInfo, 'r') as f:
            lines = f.read().split('\n')
            info = []
            for line in lines:
                if line.__contains__(','):
                    info.append(line.split(','))
            for i in range(len(info)):
                if str(self.id) == info[i][0]:
                    return info, info[i]
            info.append([self.id,self.created_at,self.updated_at])
            return info, info[i]
