from PyQt5.QtCore import QThread, pyqtSignal
from pymongo import MongoClient
from time import gmtime, strftime
from random import randint
import sys


class MyDBThread(QThread):
    db = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["database"]
        self.doc = {}

    def update_db(self, data, current):
        current_time = strftime("%H:%M:%S", gmtime())

        self.cnt = randint(1, 1000000)
        self.doc["_id"] = self.cnt

        if current == "Temperature":
            self.collection = self.db.temp
            self.doc["TEMP"] = data
        if current == "Pressure":
            self.collection = self.db.press
            self.doc["PRESS"] = data
        if current == "Irradiance":
            self.collection = self.db.light
            self.doc["LIGHT"] = data

        self.doc["time"] = current_time

        try:
            self.collection.insert_one(self.doc)
        except:
            e = sys.exc_info()[0]
            print(e)

    def exit(self):
        self.terminate()
