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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ display HTML page with list of states """
    states = storage.all(classes["State"]).values()
    if id is not None:
        id = 'State.' + id
    # ^ fetches States data from storage engine, then in line below,
    # those states are passed into the template
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def remove_SQLalc_session(exception):
    """ close storage when tear down occurs """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)