#!/usr/bin/env python3
"""
First Flask website in python.
@author Ellery Penas
@version 2018.04.11
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Homepage content here."


@app.route('/about')
def about():
    return "About page content here."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
