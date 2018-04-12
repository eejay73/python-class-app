#!/usr/bin/env python3
"""
First Flask website in python.
@author Ellery Penas
@version 2018.04.11
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
