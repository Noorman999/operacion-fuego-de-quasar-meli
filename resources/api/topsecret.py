from flask_restx import Namespace, Resource, reqparse
from flask import request
import os

from resources.models.satelite import Satelite
from resources.models.shuttle import Shuttle
from resources.exceptions.satelite import InvalidSateliteData
from resources.utils.functions import findObject

api = Namespace('', description='Top Secret Actions')

#PARSERS

post_parser = reqparse.RequestParser()
post_parser.add_argument('distance',  type=float, help='Distancia a la Nave', required=True, location='json')
post_parser.add_argument('message',  type=str, help='Mensaje que la nave quiere transmitir', required=True, location='json')

@api.route('/topsecret_split/<string:satelite>')
class TopSecretSplitPost(Resource):

    @api.doc(
        responses={
            200: "SUCCESS",
            404: "NOT FOUND",
            500: "INTERNAL ERROR"
        }
    )
    
    @api.expect(post_parser)
    def post(self, satelite):
        try:
            args = request.json
            satelite = Satelite(satelite, args["distance"], args["message"])
            satelite.save()
            return { "status": args }, 200

        except Exception as default_error:
            return {"error": str(default_error)}, 500


@api.route('/topsecret_split/')
class TopSecretSplitGet(Resource):

    @api.doc(
        responses={
            200: "SUCCESS",
            404: "NOT FOUND",
            500: "INTERNAL ERROR"
        }
    )

    def get(self):
        try:
            shuttle = Shuttle()
            kenobi = Satelite("Kenobi")
            skywalker = Satelite("Skywalker")
            sato = Satelite("Sato")
            x, y = shuttle.GetLocation(kenobi.getDistance(), skywalker.getDistance(), sato.getDistance())
            message = shuttle.GetMessage(kenobi.getMessage(), skywalker.getMessage(), sato.getMessage())
            kenobi.remote_delete()
            skywalker.remote_delete()
            sato.remote_delete()
            return { "position": { "x": x, "y": y }, "message": message }, 200
        except InvalidSateliteData as e:
            return {"error": str("No se tiene la informacion necesaria triangular la posicion de la nave")}, 404
        except Exception as e:
            return {"error": str(e)}, 500


post_parser = reqparse.RequestParser()
post_parser.add_argument('satellites',  type=list, help='Lista de Satelites', required=True, location='json')

@api.route('/topsecret/')
class TopSecret(Resource):

    @api.doc(
        responses={
            200: "SUCCESS",
            404: "NOT FOUND",
            500: "INTERNAL ERROR"
        }
    )
    
    @api.expect(post_parser)
    def post(self):
        try:
            args = request.json
            satellites = args["satellites"]
            if type(args["satellites"]) != list:
                return {"error": "'satellites' debe de ser una lista de satelites"}, 400

            kenobi = findObject(satellites, "name", "kenobi")
            skywalker = findObject(satellites, "name", "skywalker")
            sato = findObject(satellites, "name", "sato")

            shuttle = Shuttle()
            x, y = shuttle.GetLocation(kenobi["distance"], skywalker["distance"], sato["distance"])
            message = shuttle.GetMessage(kenobi["message"], skywalker["message"], sato["message"])
            return { "position": { "x": x, "y": y }, "message": message }, 200

        except Exception as default_error:
            return {"error": str("No se tiene la informacion necesaria triangular la posicion de la nave")}, 404