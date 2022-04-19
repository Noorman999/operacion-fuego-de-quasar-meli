import math
import numpy

from resources.utils.satelites import satelitesCoordinates


class Shuttle:

    def GetLocation(self, kenobiDistance, skywalkerDistance, satoDistance):
        if kenobiDistance == None or skywalkerDistance == None or satoDistance == None:
            raise Exception("No hay informacion suficiente para sacar el calculo")

        LatKenobi = satelitesCoordinates["Kenobi"]["x"]
        LonKenobi = satelitesCoordinates["Kenobi"]["y"]
        LatSkywalker = satelitesCoordinates["Skywalker"]["x"]
        LonSkywalker = satelitesCoordinates["Skywalker"]["y"]
        LatSato = satelitesCoordinates["Sato"]["x"]
        LonSato = satelitesCoordinates["Sato"]["y"]

        P1 = numpy.array([LatKenobi, LonKenobi])
        P2 = numpy.array([LatSkywalker, LonSkywalker])
        P3 = numpy.array([LatSato, LonSato])

        #from wikipedia
        ex = (P2 - P1)/(numpy.linalg.norm(P2 - P1))
        i = numpy.dot(ex, P3 - P1)
        ey = (P3 - P1 - i*ex)/(numpy.linalg.norm(P3 - P1 - i*ex))
        d = numpy.linalg.norm(P2 - P1)
        j = numpy.dot(ey, P3 - P1)

        #validaciones
        #se valida interseccion los radios de los satelites
        d2 = numpy.linalg.norm(P3 - P1)
        d3 = numpy.linalg.norm(P3 - P2)
        if d > (kenobiDistance + skywalkerDistance) or d2 > (kenobiDistance + satoDistance) or d3 > (satoDistance + skywalkerDistance):
            raise Exception('No se puede encontrar el satelite ya que la informacion dada no es valida')

        if d < abs(kenobiDistance - skywalkerDistance) or d2 < abs(kenobiDistance - satoDistance) or d3 < abs(satoDistance - skywalkerDistance):
            raise Exception('No se puede encontrar el satelite ya que la informacion dada no es valida')

        x = (pow(kenobiDistance,2) - pow(skywalkerDistance,2) + pow(d,2))/(2*d)
        y = ((pow(kenobiDistance,2) - pow(satoDistance,2) + pow(i,2) + pow(j,2))/(2*j)) - ((i/j)*x)

        finalPoint = P1 + x*ex + y*ey

        return round(finalPoint[0], 2), round(finalPoint[1], 2)

    
    def GetMessage(self, kenobiMessage, skywalkerMessage, satoMessage):
        if kenobiMessage == None or skywalkerMessage == None or satoMessage == None:
            raise Exception("No hay informacion suficiente para sacar el calculo")
        full_message = []
        messages = [kenobiMessage, skywalkerMessage, satoMessage]
        message_len = max(len(kenobiMessage), len(skywalkerMessage), len(satoMessage))
        for i in range(message_len):
            for message in messages:
                if message[i] != "":
                    full_message.append(message[i])
                    break
        return " ".join(full_message)

            
