#!/usr/bin/env python3


### Importing Files
from flask import Flask, render_template, url_for


### Creating App Object
app = Flask(__name__)


### Routing
# Home Page
@app.route("/")
def homePage():
    return render_template('index.html')

# About Page
@app.route("/about")
def aboutPage():
    return render_template('about.html')

# Contact Page
@app.route("/contact")
def contacttPage():
    return render_template('contact.html')


### Running Web
if __name__ == "__main__":
    app.run(debug = True, port = 8000)

