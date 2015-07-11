from flask import jsonify, request
from flask.ext.restful import Resource
from datetime import date

from model import StationSnapshot
from util import parse_params, handle_help


class StationAPI(Resource):

    def get(self, contract_name, station_id):
        query = StationSnapshot.query\
            .filter_by(number=station_id)\
            .filter_by(contract_name=contract_name)\
            .order_by(StationSnapshot.last_update)

        period = request.args.get('period')
        if period == 'today':
            query = [elt for elt in query if elt.last_update.date() == date.today()]
        return jsonify(data=[shapshot.json for shapshot in query])
