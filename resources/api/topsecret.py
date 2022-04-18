from flask_restx import Namespace, Resource, reqparse
from flask import request
import os

from resources.models.satelite import Satelite

api = Namespace('', description='Top Secret Actions')

#PARSERS

post_parser = reqparse.RequestParser()
post_parser.add_argument('name',  type=str, help='Nombre del Satelite', required=True, location='json')
post_parser.add_argument('distance',  type=float, help='Distancia a la Nave', required=True, location='json')
post_parser.add_argument('message',  type=str, help='Mensaje que la nave quiere transmitir', required=True, location='json')

@api.route('/topsecret_split/')
class ShouldLogin(Resource):

    @api.doc(
        responses={
            200: "SUCCESS",
            207: "SUCCESSFUL RESULT WITH MESSAGE",
            213: "ERROR RESULT WITH MESSAGE",
            307: "TEMPORARY REDIRECT",
            308: "PERMANENT REDIRECT",
            400: "BAD REQUEST",
            401: "UNAUTHORIZED",
            403: "FORBIDDEN",
            404: "NOT FOUND",
            500: "INTERNAL ERROR"
        },
        security=['apikey']
    )
    @api.expect(post_parser)
    def post(self):
        try:
            args = request.json
            satelite = Satelite(args["name"])
            satelite.setDistance(args["distance"])
            satelite.setMessage(args["message"])
            return { "status": args }, 200

        except Exception as default_error:
            return {"result": str(default_error)}, 213