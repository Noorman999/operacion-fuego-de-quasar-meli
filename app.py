from flask import Flask, request
from resources import api

app = Flask(__name__)

api.init_app(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8082", debug=True)
