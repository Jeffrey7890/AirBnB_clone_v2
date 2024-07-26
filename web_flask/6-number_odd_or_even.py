#!/usr/bin/python3
""" Start up flask server on 0.0.0.0:5000 """
from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ response with Hello from hbnb """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ retrune to /hbnb route """
    return ("HBNB")


@app.route('/c/<name>', strict_slashes=False)
def var_url(name):
    """ response with variable unifrom resource location url """
    result = "C " + escape(name).replace('_', " ")
    return (result)


@app.route('/python', defaults={'text': None}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def var_url_again(text):
    """ response to variable url with python/ """
    if text is None:
        return ("Python is cool")
    result = "Python " + escape(text).replace('_', ' ')
    return (result)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    result = str(n) + " is a number"
    return (result)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    return (render_template('5-number.html', number=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    return (render_template('6-number_odd_or_even.html', number=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
