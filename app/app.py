import os
from flask import Flask, render_template, request, jsonify
import json
import numpy as np
import pymongo

server = Flask(__name__)

@server.route("/")
@server.route("/index")
def index():
    return render_template("index.html")

@server.route("/about")
def about():
    return render_template("about.html")

@server.route("/projects")
def projects():
    return render_template("projects.html",
                           title="Projects")

@server.route("/tda-classification")
def tda_classification():
    return render_template("tda_classification.html")

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8000, debug=True)
