from flask import Blueprint, jsonify, current_app
from flask.ext.restful import Api
from util import handle_help


common_blueprint = Blueprint('common', __name__)
common_blueprint_api = Api(common_blueprint)


@common_blueprint.route('/routes')
@handle_help('routes')
def list_routes():
    output = []
    for rule in current_app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = "{:50s} {:20s}".format(str(rule), methods)
        output.append(line)
    return jsonify(
        routes=output,
        help="add '?help=true' to a route to know about the parameters you can use"
    )
