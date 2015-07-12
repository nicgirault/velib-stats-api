from flask import jsonify, request
from flask.ext.restful import Resource
from datetime import date, datetime

from model import StationSnapshot
from util import parse_params, handle_help


class StationAPI(Resource):

    def get(self, contract_name, station_id):
        query = StationSnapshot.query\
            .filter_by(number=station_id)\
            .filter_by(contract_name=contract_name)\
            .order_by(StationSnapshot.last_update)

        start = request.args.get('start')
        if start:
            start = datetime.fromtimestamp(int(start)/1000)
            query = query.filter(StationSnapshot.last_update >= start)

        end = request.args.get('end')
        if end:
            start = datetime.fromtimestamp(int(end)/1000)
            query = query.filter(StationSnapshot.last_update <= end)

        period = request.args.get('period')
        if period == 'today':
            query = [elt for elt in query if elt.last_update.date() == date.today()]

        return jsonify(data=[shapshot.json for shapshot in query])
