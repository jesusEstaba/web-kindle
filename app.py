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

#uri = os.environ.get('MONGO_DB_URI', "mongodb://127.0.0.1")
#client = MongoClient(uri)
#db = client.kindle
#############################


@app.route("/")
def home_view():
    return render_template("home.html")