# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)
#print(Base.classes.keys())

# Save references to each table
Measurement=Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

##################################################
# Flask Routes 
##################################################

# 1 Home pg. 
#list all avaiable routes
@app.route("/")
def welcome():
    """List all avaiable routes!"""
    return(
        f"Avaiable Routes:<br/>"
        f"/api.v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"api/v1.0<start>/br/>"
        f"api/v1.0/<start>/<end>br/>"
)

#2 Return json with the date as the key and the value as the precipitation
# precipitation route  returns the jsonified preipitation data for the last year in the database. 
@app.route("/api/v1.0/precipitation")
def precipitation():
    session=Session(engine)
    one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    results = session.query(Measursement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all() 

    prcp_data =[]
    for date, prcp in results:
        prcp_dict ={
            "date": date,
            "prcp": prcp
        }
        prcp_data.append(prcp_dict)



    session.close()
    return jsonify(prcp_data)

#3 return a station route - jsonified data of all of the station in the database
@app.route("/api/v1.0/station")

def station():
    session = Session(engine)
    """Return information on all the stations"""
    results = session.query(Station.station, Station.name, Station.id, Station.latatuide, Station.longitude, Station.elevation).all()


    station_info =[]    
    for station, name, id, latitude, longitude, elevation  in results:
        station_dict = {
        "station" : station,
        "name" : name,
        "id" : id,
        "latitude" : latitude,
        "longitude": longitude,
        "elevation": elevation
    }  
    station_info.append(station_dict)

    session.closed()

    return jsonify(station_info)

#4 tobs route returns jsonfied data for the most active station (USC00519281) and make sure you only
#   return the jsonifeid data for the last year of data. 
@app.route("/api/v1.0/tobs")
def tobs():
    session =Session(engine)
    
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results =session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= one_year_ago).filter(Measurement.station == 'USC00519281').all()
    
    tobs_data =[]
    for date, tobs in results:
        tobs_dict ={
            "date": date,
            "tobs": tobs
    }
    tobs_data.append(tobs_dict)
    session.close()
    
    return jsonify(tobs_data)

#Returns jsonified data as a paramater for the url
#returns the min, max and avg temperture calculation from the start date and end of the dataset. 
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")

def temperature_starts(start, end=None):
    session =Session(engine)
    start_date =dt.datetime.strptime(start, "%Y-%m-%d")
    
    if end:
        end_date =session.query(func.max(Measurement.date)).scalar()
    
#query min, max and avg
    temp_stats =session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)\
        .filter(Measurement.date >= start_date).filter(Measurement.date <=end_date).all())

    session.close()

    temp_dict ={
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d") if end_date else None,
        "min_temperature": temperature_stats[0][0],
        "max_temperature": temperature_stats[0][1],
        "avg_temperature": temperature_stats[0][2]
        }

    session.close()

    return jsonify(temp_dict)                                

if __name__=="__main__":
    app.run(debug=True)