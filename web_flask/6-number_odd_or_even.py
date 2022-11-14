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
    """method prints C and value"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python_text_value(text="is cool"):
    """method prints Python and value given"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def print_int(n):
    """method prints if there is an int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ method displays an HTML if int"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def print_odd_or_even(n):
    """ method prints whether value given is odd or even"""
    if n % 2 == 0:
        o = "even"
    else:
        o = "odd"
    return render_template('6-number_odd_or_even.html', n=n, o=o)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
