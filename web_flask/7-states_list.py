#!/usr/bin/python3
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes:
    - /states_list
"""
from models import *
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
app = Flask(__name__)
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays list of states via HTML doc """
    states = storage.all(classes["State"]).values()
    # gets data from db / passes them into the html template
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_SQLalc(exception):
    """ close SQLalc after each request """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
