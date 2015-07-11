from flask import Blueprint
from flask.ext.restful import Api


station_blueprint = Blueprint('stats', __name__)
station_blueprint_api = Api(station_blueprint)

from resource.station import StationAPI
station_blueprint_api.add_resource(StationAPI, '/station/<int:station_id>')
