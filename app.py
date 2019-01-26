# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo
import JobVizzY
from JobVizzY import scrapListFrameDict
from userInput import jobListSampleCut
from userInput import cityListSampleCut

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/jobViz_app"
mongo = PyMongo(app)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.jobViz_db
# Run scraper functions to fill up above db in mongo
# fulljobVizdata = JobVizzY.scrapListFrameDict(
#     jobListSampleCut, cityListSampleCut)
print('')
# print(len(fulljobVizdata))
# print('')
# Insert job listings into mongoDb
# db.collection.drop()
# db.collection.insert_many(fulljobVizdata)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/00/")
def user():

    return render_template("00Forms.html")
#


@app.route("/01/")
def scrap():

    return render_template("01Scraper.html")


@app.route("/02/")
def listerDemo():

    return render_template("02ListerDemo.html")


@app.route("/03/")
def lister():
    inventory = list(db.collection.find())
    # print(inventory)

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
