#---Climate API---#

#Dependencies

import datetime as dt
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

def welcome():
    """List all available API Routes."""
    
    return (
            
            f"Welcome to the Surfs Up API.<br>"
            f"These are the available routes:<br>"
            f"Available routes:<br>"
            f"/api/precipitation<br>"
            f"/api/stations<br>"
            f"/api/temperature<br>"
    )

#Route: "/api/precipitation"

@app.route("/api/precipitation")
def precipitation():
    """Api Route that returns data for rainfall for the last year."""

    #Get the latest date in DB
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    #query date
    query_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    #query
    precip_query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).order_by(Measurement.date).all()


    #Create list of dictionaries; (Keys: 'date', Values: 'prcp')
    precip_list = []
    #loop through the query to get data and save it in precip_list
    for item in precip_query:
        precip_dict = {}
        precip_dict["date"] = precip_query[0]
        precip_dict["prcp"] = precip_query[1]
        precip_list.append(precip_dict)

    #Return jsonified precip_list
    return jsonify(precip_list)

