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

    app.run(host='0.0.0.0', port='5000')
=======
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes:
    /
    /hbnb
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ route function to return Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_only():
    """ route function to return HBNB """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 4e9d85e94116c80a4c0a4b6eee6d0ea8588cdc67
