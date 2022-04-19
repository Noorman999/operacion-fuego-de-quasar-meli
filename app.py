from flask import Flask, request, render_template
from resources import api

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
