# import necessary libraries
from flask import (
    Flask, 
    render_template, 
    redirect, 
    jsonify,
    request,
    make_response,
    url_for,
    session
    )
from flask_pymongo import PyMongo
import JobVizzY
from flask_session import Session

# create instance of Flask app
app = Flask(__name__)       

mongo_uri = 'mongodb://heroku_attila5287:jobvizzy1@ds113495.mlab.com:13495/heroku_m3j2ckrz'
app.config['MONGO_URI'] = mongo_uri
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug
# Create db connection
mongo = PyMongo(app,uri=mongo_uri)

# Create a list to hold our data
userInputJob = []
userInputCity = []


@app.before_first_request
def setup():
    userInputJob.clear()
    userInputCity.clear()
    return ()

# SESSION_TYPE = 'Redis'
# app.config.from_object(__name__)
# Session(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'


@app.route('/get/')
def get():
    return session.get('key', 'not set')



#  index more like intro now
@app.route("/index/", methods=["GET", "POST"])
def home():
    pass
    return render_template("index.html")


@app.route("/")
def forms():
    pass
    return render_template("00Forms.html", jobDisplayList=userInputJob,cityDisplayList=userInputCity)


@app.route("/send/job", methods=["GET", "POST"])
def sendUserJob():
    pass

    if request.method == "POST":
        userJobForm = request.form["Job"]
        userInputJob.append(userJobForm)

        return redirect("/")

    return 


@app.route("/send/city", methods=["GET", "POST"])
def sendUserCity():
    pass
    if request.method == "POST":

        userCityForm = request.form["City"]

        userInputCity.append(userCityForm)

        return redirect("/")

    return 


@app.route("/user/reset", methods=["GET", "POST"])
def userRes3t():
    if request.method == "POST":
        userInputJob.clear()
        print(userInputJob)
        userInputCity.clear()
        print(userInputCity)
    return redirect("/", code=302)

@app.route("/user/job")
def userDataJob():
    print(userInputJob)
    return jsonify(userInputJob)

@app.route("/user/city")
def userDataCity():
    print(userInputCity)
    return jsonify(userInputCity)    


# not much functional
@app.route("/01/")
def scrap():
    pass
    return render_template("01Scraper.html")


@app.route("/02/")
def listerDemo():

    return render_template("02ListerDemo.html")


@app.route("/03/")
def lister():
    pass
    fulljobVizdata = JobVizzY.scrapListFrameDict(userInputJob, userInputCity)
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

