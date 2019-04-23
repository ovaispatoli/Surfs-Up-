#---Climate API---#

#Dependencies

import datetime as datetime
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#-Database Setup-#

#Connecting to DB
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

#Test connection
print(Base.classes.keys())

#References to tables in DB
Station = Base.classes.station
Measurement = Base.classes.measurement

#Create session

session = Session(engine)

#-Flask Setup-#
app = Flask(__name__)


#-Flask Routes-#

#Route: '/'
@app.route("/")
def home():
    print("Server received request for 'Home' page.")
    return "Welcome to the Surfs Up Weather API."

#Route: "/welcome"
@app.route("/welcome")

def welcome():
    """List all available API Routes."""
    
    return (
            f"Welcome to the Surfs Up API."
            f"Available routes:<br>"
            f"/api/precipitation<br>"
            f"/api/stations"
            f"/api/temperature"
    )



