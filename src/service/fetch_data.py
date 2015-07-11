from flask.ext.script import Command
from datetime import datetime
from client import velib
from model import StationSnapshot
from model.abc import db

def fetch_and_save_stations_data():
    station_snapshots = [
        StationSnapshot(station) for station in velib.get_stations_data()
    ]
    db.session.add_all(station_snapshots)
    db.session.commit()

class FetchDataCommand(Command):
    def run(self):
        print('Start fetching data at ' + str(datetime.now()))
        fetch_and_save_stations_data()
        print('Data fetched at ' + str(datetime.now()))
