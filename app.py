#!/usr/bin/env python3


### Importing Files
from flask import Flask, render_template, url_for


### Creating App Object
app = Flask(__name__)


### Routing
# Home Page
@app.route("/")
def hello_world():
    return render_template('index.html')


### Running Web
if __name__ == "__main__":
    app.run(debug = True, port = 8000)

