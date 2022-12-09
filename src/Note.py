from datetime import datetime
from typing import List
import Note
import os


class Note:
    notes_path = 'notes/'
    notesInfo = notes_path + 'NotesInfo.txt'
    tokens_path = notes_path + 'tokens.txt'
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
                self.created_at = i[1]
                self.updated_at = i[2]
            f.close()
        except FileNotFoundError:
            f = open(self.notes_path + str(self.id) + '.txt', 'w')
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.saveInfo()
            f.close()
        return text

    def deleteNote(self):
        info = self.getInfo()
        with open(self.notesInfo, 'w') as f:
            for i in info:
                if str(self.id) != i[0]:
                    f.write(f'{i[0]},{i[1]},{i[2]}\n')
        os.remove(self.notes_path + str(self.id) + '.txt')

    def writeFile(self):
        with open(self.notes_path + str(self.id) + '.txt', 'w') as f:
            f.write(self.text)
        self.saveInfo()

    def editNote(self, text: str):
        self.text = text
        self.updated_at = datetime.now()
        self.writeFile()

    @staticmethod
    def getList():
        info = Note.getInfo()
        dictList = {}
        for i in range(len(info)):
            dictList[i] = info[i][0]
        print(dictList)
        return dictList

    @staticmethod
    def getTokenList():
        try:
            with open(Note.tokens_path, 'r') as f:
                tokens = f.read().split('\n')
                return tokens
        except FileNotFoundError:
            return []

    @staticmethod
    def getInfo():
        try:
            with open(Note.notesInfo, 'r') as f:
                lines = f.read().split('\n')
                info = []
                for line in lines:
                    if line.__contains__(','):
                        info.append(line.split(','))
                return info
        except FileNotFoundError:
            return []

    @staticmethod
    def isntExist(id: int):
        isntExist = True
        for i in Note.getInfo():
            if i[0] == str(id):
                isntExist = False
        return isntExist

    def getNoteInfo(self):
        info = self.getInfo()
        for i in info:
            if i[0] == str(self.id):
                return i

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
            return info, -1
