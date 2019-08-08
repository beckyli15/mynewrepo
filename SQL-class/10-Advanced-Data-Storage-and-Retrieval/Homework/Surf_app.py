
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#from flask import Flask, jsonify
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger


#Step 2 - Climate App
app = Flask(__name__)
@app.route("/")
def homepage():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    last_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_query = session.query(Measurements.date, Measurements.prcp).\
        filter(Measurements.date > last_year).\
             order_by(Measurements.date).all()

    precipitation_a=[]
    for date, prcp in precipitation:
        precipitation_dict={}
        precipitation_dict["date"]=precipitation_query[0]
        precipitation_dict["prcp"]=precipitation_query[1]
        precipitation.append(precipitation_dict)
    
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations_query = session.query(Station.name, Station.station)
    stations = pd.read_sql(stations_query.statement, stations_query.session.bind)
    return jsonify(stations.to_dict())


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    last_date = session.query(func.max(Measurement.date)).all()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temperature = session.query(Measurements.date, Measurements.tobs).\
        filter(Measurements.date > last_year).\
        order_by(Measurements.date).all()
    temp_ob=[]
    temp_dict={}
    temp_dict["date"]=temperature[0]
    temp_dict["tobs"]=temperature[1]
    temp_ob.append(temp_dict)

    return jsonify(temp_ob)


@app.route("/api/v1.0/<start>")
def trip(start):
    session = Session(engine)
    


@app.route("/api/v1.0/<start>/<end>")
def trip(start,end):
    session = Session(engine)


if __name__ == '__main__':
    app.run(debug=True)