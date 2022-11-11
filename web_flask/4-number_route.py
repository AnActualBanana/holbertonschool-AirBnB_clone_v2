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
def print_c_text_value(text):
    """method prints C and value given"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python_text_value(text="is cool"):
    """method prints Python and value"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    """method prints if there is an int"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")