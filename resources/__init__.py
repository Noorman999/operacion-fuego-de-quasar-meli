from resources.api.topsecret import api as topsecret
from flask_restx import Api

api = Api(
    version='1.0',
    title='Operacion Fuego de Quasar',
    description='Mercado Libre Test API',
    doc='/swagger/'
)

api.add_namespace(topsecret)
