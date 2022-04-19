import ast
from resources.db.sqlite3 import SqliteHandler
from resources.utils.satelites import validSatelites

class Satelite:

    def __init__(self, name: str):
        if not name:
            raise Exception("Se necesita un nombre para el satelite")
        if name not in validSatelites:
            raise Exception("Nombre de Satelite Invalido")
        self.dbconn = SqliteHandler()
        self.dbconn.create_model("Satelite", {"distance": "REAL", "message": "text"})
        self.dbconn.create_object("Satelite", name)
        self.name = name


    def setDistance(self, distance: float):
        if type(distance) != float:
            raise Exception("La distancia debe de ser un flotante")
        self.dbconn.set_model_attribute("Satelite", self.name, "distance", distance)


    def setMessage(self, message: str):
        self.dbconn.set_model_attribute("Satelite", self.name, "message", message)


    def getDistance(self) -> float:
        return self.dbconn.get_model_attribute("Satelite", self.name, "distance")

    
    def getMessage(self) -> list:
        message = self.dbconn.get_model_attribute("Satelite", self.name, "message")
        return ast.literal_eval(message) if type(message) == str else message


