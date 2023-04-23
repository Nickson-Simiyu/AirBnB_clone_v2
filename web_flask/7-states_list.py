#!/usr/bin/python3
""" 7. Start flask service that does something. """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the SQLAlchemy session after each request."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of all State objects in alphabetical order."""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_sorted)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
