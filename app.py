#!/usr/bin/env python3


### Importing Modules, Files, etc.
from flask import (
    Flask,
    render_template,
    url_for,
    request
)
from helper.search import *


### Creating App Object
app = Flask(__name__)


### Routing
# Home Page with search Engine
@app.route("/")
def homePage():
    query = request.args.get('search')
    if query:
        search = SearchEngine(query)
    gif = RandomAnimeGif()
    return render_template('index.html', gifUrl = gif.imgUrl)

# About Page
@app.route("/about")
def aboutPage():
    return render_template('about.html')

# Contact Page
@app.route("/contact")
def contactPage():
    return render_template('contact.html')


### Running Web
if __name__ == "__main__":
    app.run(debug = True, port = 8000)

