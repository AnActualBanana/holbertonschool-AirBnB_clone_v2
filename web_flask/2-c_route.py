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
def print_text_value(text):
    """method prints C and value given"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
