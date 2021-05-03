#!/usr/bin/python3
<<<<<<< HEAD
""" starts a Flask web application listening on port 5000 """


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello():
        """ displays 'Hello HBNB!' """
        return 'Hello HBNB!'

    app.run(host="0.0.0.0", port="5000")
=======
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ route function to return Hello HBNB! """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 4e9d85e94116c80a4c0a4b6eee6d0ea8588cdc67
