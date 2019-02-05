# import necessary libraries
from flask import (
    Flask, 
    render_template, 
    redirect, 
    jsonify,
    request)
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo

import pandas as pd
from bs4 import BeautifulSoup
import requests

import JobVizzY
from JobVizzY import scrapListFrameDict
from userInput import jobListSampleCut
from userInput import cityListSampleCut
from userInput import userListCities
from userInput import userListJobs

# create instance of Flask app
app = Flask(__name__)

mongo_uri = 'mongodb://heroku_attila5287:jobvizzy1@ds113495.mlab.com:13495/heroku_m3j2ckrz'
app.config['MONGO_URI'] = mongo_uri
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug
# Create db connection
mongo = PyMongo(app,uri=mongo_uri)

# Create a list to hold our data
userInputJobs = []
userInputCity = []
userJob = ""
userCity = ""



@app.route("/index")
def home():

    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
@app.route("/send/job", methods=["GET", "POST"])
def sendUserJob():
    pass
    if request.method == "POST":
        userJobForm = request.form["Job"]

        userInputJobs.append(userJobForm)

        return render_template("00Forms.html", jobDisplayList=userInputJobs)

    return render_template("00Forms.html")

@app.route("/user/job")
def data():
    print(userInputJobs)
    return jsonify(userInputJobs)

@app.route("/01/")
def scrap():
    pass
    return render_template("01Scraper.html")


@app.route("/02/")
def listerDemo():

    return render_template("02ListerDemo.html")
1

@app.route("/03/")
def lister():
    pass
    fulljobVizdata = JobVizzY.scrapListFrameDict(
    userInputJobs, userListCities)
# Insert job listings into mongoDb1
    
    mongo.db.collection.drop()
    mongo.db.collection.insert_many(fulljobVizdata)
    inventory = list(mongo.db.collection.find())
   
    return render_template("02Lister.html", inventory=inventory)


@app.route("/04/")
def bubbler():
    cityList = ["chicago", "omaha", "houston", "new+york", "los+angeles"]
    jobList = ['front+end+developer',
               'back+end+developer',
               'full+stack+developer'
               ]
    return render_template("03Bubbler.html", cityList=cityList, jobList=jobList)


if __name__ == "__main__":
    app.run(debug=True)
