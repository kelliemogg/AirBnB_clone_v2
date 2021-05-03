#!/usr/bin/python3
<<<<<<< HEAD
""" displays a string based on route slash """


if __name__ == '__main__':
    from flask import Flask, abort
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hello():
        """ display Hello HBNB """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hello_hbnb():
        """ display HBNB """
        return "HBNB"

    @app.route('/c/<path:text>', strict_slashes=False)
    def C(text):
        """ display contents of text """
        new_text = 'C ' + text.replace('_', ' ')
        return new_text

    @app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
    @app.route('/python/<path:text>', strict_slashes=False)
    def python(text):
        """ display text var """
        py_text = 'Python ' + text.replace('_', ' ')
        return py_text

    @app.route('/number/<n>', strict_slashes=False)
    def numb(n):
        """ display n if number """
        try:
            num = int(n)
            new_num = str(num) + ' is a number'
            return new_num
        except:
            abort(404)

    app.run(host='0.0.0.0', port='5000')
=======
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes:
    /
    /hbnb
    /c/<text>
    /python/(<text>)
    /number/<int:n>
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ route to return Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_only():
    """ route to return HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text_var(text):
    """ route to return C followed by text variable, replaces _ with spaces """
    text = text.replace('_', ' ')
    return ('C' + ' ' + text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def python_iscool(text=None):
    """ route to return text followed by "is cool" by default, (which can be
    overwritten), replaces _ with spaces """
    if text is None:
        text = 'is cool'
    else:
        text = text.replace('_', ' ')
    return ('Python' + ' ' + text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ route that displays “n is a number” only if n is an integer """
    return ("{:d} is a number".format(n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 4e9d85e94116c80a4c0a4b6eee6d0ea8588cdc67
