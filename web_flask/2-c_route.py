#!/usr/bin/python3
<<<<<<< HEAD
""" displays a string based on route slash """


if __name__ == '__main__':
    from flask import Flask
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
        """ display HBNB """
        new_text = 'C ' + text.replace('_', ' ')
        return new_text

    app.run(host='0.0.0.0', port='5000')
=======
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes:
    /
    /hbnb
    /c/<text>
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 4e9d85e94116c80a4c0a4b6eee6d0ea8588cdc67
