from .abc import db, BaseModel
from datetime import datetime


class StationSnapshot(db.Model, BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, index=True)
    contract_name = db.Column(db.String(120), nullable=False, index=True)
    status = db.Column(db.String(20), nullable=False)
    bike_stands = db.Column(db.Integer, nullable=False)
    available_bike_stands = db.Column(db.Integer, nullable=False)
    available_bikes = db.Column(db.Integer, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False, index=True)

    def __init__(self, stationData):
        self.number = stationData.get('number')
        self.contract_name = stationData.get('contract_name')
        self.status = stationData.get('status')
        self.bike_stands = stationData.get('bike_stands')
        self.available_bike_stands = stationData.get('available_bike_stands')
        self.available_bikes = stationData.get('available_bikes')
        self.last_update = datetime.fromtimestamp(stationData.get('last_update')/1000)
