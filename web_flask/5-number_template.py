#!/usr/bin/python3
""" displays a string based on route slash """


if __name__ == '__main__':
    from flask import Flask, abort, render_template
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

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """ display template if n is a number """
        return render_template('5-number.html', n=n)

    app.run(host='0.0.0.0', port='5000')
