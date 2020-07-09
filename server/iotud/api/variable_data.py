import functools
from datetime import datetime
from flask import Blueprint, jsonify,  request
from iotud.tools import fetch_all, fetch_one, update, insert, get_auth_props, either_response, delete
from iotud.api.variables import check_ownership_variable
from oslash import Right, Left


bp = Blueprint('variable_data', __name__, url_prefix="/users")


@bp.route('/get_variable_data', methods=['POST'])
def get_variable_data():
    data = get_auth_props(['id_variable', 'start', 'end', 'results', 'type'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    variables = data.bind(check_ownership_variable).bind(get_variable_data_db)
    return either_response(variables)


def get_variable_data_db(data: dict):
    if data['data']['type'] == 'date':
        query = "SELECT * FROM variable_data \
                WHERE id_variable = %s AND timestamp >= %s and TIMESTAMP <= %s\
                ORDER BY timestamp DESC"
        vals = (data["data"]["id_variable"], data['data']
                ['start'], data['data']['end'])
    else:
        query = "SELECT * FROM variable_data \
                WHERE id_variable = %s \
                ORDER BY timestamp DESC \
                LIMIT %s"
        vals = (data["data"]["id_variable"], data["data"]["results"])
    variables = fetch_all(query, vals)
    return variables
