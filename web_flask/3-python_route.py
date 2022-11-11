#!/usr/bin/python3
"""Python script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    """method prints 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """method prints 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_ctext_value(text):
    """method prints 'C' and value given"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_pythontext_value(text="is cool"):
    """method prints 'Python' and value given"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
