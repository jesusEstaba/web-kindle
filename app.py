from flask import Flask, render_template, redirect, session, request, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import random

#############################
# APP FLASK CONFIGURATION
app = Flask(__name__)
app.secret_key = ".."

# DATABASE CONFIGURATION

uri = os.environ.get('MONGO_DB_URI', "mongodb://127.0.0.1")
client = MongoClient(uri)
db = client.kindle
#############################


@app.route("/")
def home_view():
    return render_template("home.html")

@app.route("/amp")
def amp_view():
    return render_template("amp.html")

@app.route("/notes")
def notes_view():
    notes = db.notes.find().sort('_id', -1)
    return render_template("notes.html", notes=notes)

@app.route("/notes/add")
def notes_add_view():
    note = {
        'content': request.args.get('content')
    }
    db.notes.insert_one(note)
    return redirect('/notes')

@app.route("/code")
def code_view():
    f = open("index.js", "r")
    rr = f.read().replace('\n', '<br>').replace("const", "<b>const</b>").replace("await", "<em>await</em>")
    return render_template("code.html", rr=rr)