from resources.db.sqlite3 import SqliteHandler
from resources.utils.satelites import validSatelites

class Satelite:

    def __init__(self, name: str):
        if not name:
            raise Exception("Se necesita un nombre para el satelite")
        if name not in validSatelites:
            raise Exception("Nombre de Satelite Invalido")
        dbconn = SqliteHandler()
        dbconn.create_model("Satelite", {"distance": "REAL", "message": "text"})
        dbconn.create_object("Satelite", name)
        self.name = name


    def setDistance(self, distance: float):
        dbconn = SqliteHandler()
        dbconn.set_model_attribute("Satelite", self.name, "distance", distance)
        dbconn.disconnect()


    def setMessage(self, message: str):
        dbconn = SqliteHandler()
        dbconn.set_model_attribute("Satelite", self.name, "message", message)
        dbconn.disconnect()