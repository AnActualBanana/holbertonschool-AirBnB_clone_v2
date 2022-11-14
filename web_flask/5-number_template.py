#!/usr/bin/python3
"""Pthon script that starts a Flask web application"""


from flask import Flask, render_template
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
    """method prints 'C' and value given"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python_text_value(text="is cool"):
    """method prints Python and value given"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def print_int_value(n):
    """method prints int if int is given"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def print_number_template(n):
    """method prints HTML if int is given"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
