from flask import jsonify
from flask.ext.restful import Resource

from model import StationSnapshot
from util import parse_params


class StationSnapshotListAPI(Resource):
    def get(self):
        return jsonify(data=[shapshot.json for shapshot in StationSnapshot.query])

class StationSnapshotAPI(Resource):
    def get(self, id):
        shapshot = StationSnapshot.query.get(id)
        return shapshot.json
