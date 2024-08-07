#!/usr/bin/python3
""" Start up flask server on 0.0.0.0:5000 """
from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ response with Hello from hbnb """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ retrune to /hbnb route """
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
