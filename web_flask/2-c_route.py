#!/usr/bin/python3
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
