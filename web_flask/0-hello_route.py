#!/usr/bin/python3
""" 0. Script to start a Flask web application """

from flask import Flask

# Create Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == '__main__':
    # Start the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
