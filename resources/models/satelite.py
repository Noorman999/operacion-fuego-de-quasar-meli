import ast
from resources.db.sqlite3 import SqliteHandler
from resources.utils.satelites import validSatelites
from resources.exceptions.satelite import InvalidSateliteData

class Satelite:

    def __init__(self, name: str, distance: float = None, message: list = None):
        self.name = name
        self.dbconn = SqliteHandler()
        self.dbconn.create_model("Satelite", {"distance": "REAL", "message": "text"})
        self.dbconn.create_object("Satelite", self.name)
        self.message = message
        self.distance = distance


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if not name:
            raise InvalidSateliteData("Se necesita un nombre para el satelite")
        name = name.lower()
        if name not in validSatelites:
            raise InvalidSateliteData("Nombre de Satelite Invalido (Kenobi, Skywalker y Sato son las unicas opciones)")
        self._name = name

    
    @property
    def message(self):
        return self._message

    
    @message.setter
    def message(self, message):
        if message == None:
            message = self.dbconn.get_model_attribute("Satelite", self.name, "message")
            message = ast.literal_eval(message) if type(message) == str else message
        if type(message) != list:
            raise InvalidSateliteData("El mensaje debe de ser una lista")
        self._message = message


    @property
    def distance(self):
        return self._distance

    
    @distance.setter
    def distance(self, distance):
        if distance == None:
            distance = self.dbconn.get_model_attribute("Satelite", self.name, "distance")
        if type(distance) != float:
            raise InvalidSateliteData("La distancia debe de ser un flotante")
        self._distance = distance



    def getDistance(self) -> float:
        return self.distance

    
    def getMessage(self) -> list:
        return self.message


    def save(self):
        self.dbconn.set_model_attributes("Satelite", self.name, {"distance": self.distance, "message": self.message})


    def remote_delete(self):
        self.dbconn.delete_model("Satelite", self.name)

    
