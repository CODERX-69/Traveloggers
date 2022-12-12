from flask import Flask, render_template, url_for, request, redirect, flash, session, jsonify
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
import random
import datetime
from uuid import uuid4


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/traveloggers"

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


@app.route("/")
def helo():
    return "Hello MF"

@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = "asdtc"
    app.run(debug=True)
