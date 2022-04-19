from flask import Flask, request
from resources import api

app = Flask(__name__)

api.init_app(app)

if __name__ == '__main__':
    app.run()
