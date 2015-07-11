from flask import Blueprint
from flask.ext.restful import Api


stats_blueprint = Blueprint('stats', __name__)
stats_blueprint_api = Api(stats_blueprint)


from resource.stationSnapshot import StationSnapshotAPI, StationSnapshotListAPI
stats_blueprint_api.add_resource(StationSnapshotListAPI, '/statistics')
stats_blueprint_api.add_resource(StationSnapshotAPI, '/statistics/<int:station_id>')
