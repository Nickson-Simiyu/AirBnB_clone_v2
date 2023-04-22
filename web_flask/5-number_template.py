#!/usr/bin/python3
""" 5. Add fifth view func that displays HTML page if n is int """

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Return other text. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ replace more text with another variable. """
    text = text.replace('_', ' ') if text else 'is cool'
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """ display html if n is int. """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
