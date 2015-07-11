from flask import Blueprint
from flask.ext.restful import Api


stats_blueprint = Blueprint('stats', __name__)
stats_blueprint_api = Api(stats_blueprint)

from resource.station import StationAPI
stats_blueprint_api.add_resource(StationAPI, '/station/<int:station_id>')
