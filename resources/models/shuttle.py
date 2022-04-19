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
        x = (pow(kenobiDistance,2) - pow(skywalkerDistance,2) + pow(d,2))/(2*d)
        y = ((pow(kenobiDistance,2) - pow(satoDistance,2) + pow(i,2) + pow(j,2))/(2*j)) - ((i/j)*x)

        return P1 + x*ex + y*ey