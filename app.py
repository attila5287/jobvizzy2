# import necessary libraries
from flask import Flask, render_template, redirect
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

mongo_uri = 'mongodb://heroku_m3j2ckrz:jobvizzy1@ds113495.mlab.com:13495/heroku_m3j2ckrz'
app.config['MONGO_URI'] = mongo_uri
app.config['FLASK_DEBUG'] = flask_debug
# Create db connection
mongo = PyMongo(app,uri=mongo_uri)
# Create a database



@app.route("/")
def home():

    return render_template("index.html")


@app.route("/00/")
def user():

    return render_template("00Forms.html")



@app.route("/01/")
def scrap():

    return render_template("01Scraper.html")


@app.route("/02/")
def listerDemo():

    return render_template("02ListerDemo.html")


@app.route("/03/")
def lister():
    inventory = list(mongo.db.collection.find())

    return render_template("02Lister.html", inventory=inventory, cityListSampleCut=cityListSampleCut)


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
