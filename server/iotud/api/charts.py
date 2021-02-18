import functools
from datetime import datetime
from flask import Blueprint, jsonify,  request
from iotud.tools import fetch_all, fetch_one, update, insert, get_auth_props, either_response, delete
from string import ascii_lowercase
import random
from oslash import Right, Left
from toolz import accumulate, assoc, reduce


bp = Blueprint('charts', __name__, url_prefix="/users")


@bp.route('/get_charts', methods=['POST'])
def get_charts():
    data = get_auth_props([],
                          request.get_json(),
                          request.headers.get('Authorization'))
    charts = data.bind(get_charts_db).map(lambda x: {"charts": x})
    return either_response(charts)


@bp.route('/create_chart', methods=['POST'])
def create_chart():
    data = get_auth_props(['id_variable', 'chart_type'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    addedChart = data.bind(add_chart_db)
    return either_response(addedChart, 'Grafica creado con exito.')


@bp.route('/update_order_charts', methods=['POST'])
def upadte_order_charts():
    data = get_auth_props(['charts_order'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    ordered_charts = data.bind(update_charts_order)
    return either_response(ordered_charts, 'Orden actualizado.')


@bp.route('/delete_chart', methods=['POST'])
def delete_chart():
    data = get_auth_props(['id_dashboard_chart'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    deleted_chart = data.bind(delete_chard_db)
    return either_response(deleted_chart, 'Orden actualizado.')


def update_charts_order(data: dict):
    charts_order = data["data"]["charts_order"]
    for chart in charts_order:
        query = 'UPDATE dashboard_charts SET index_order = %s WHERE id_dashboard_chart = %s'
        vals = (chart['index_order'], chart['id_dashboard_chart'])
        index_updated = update(query, vals)
        if not isinstance(index_updated, Right):
            return Left('UD006')
    return Right(data)


def get_charts_db(data: dict):
    query = "SELECT * FROM dashboard_charts WHERE id_user = %s ORDER BY index_order"
    vals = (data["user"]["id_user"],)
    return fetch_all(query, vals)


def add_chart_db(data: dict):
    query = "INSERT INTO dashboard_charts(id_user, id_variable, chart_type) VALUES (%s, %s, %s)"
    vals = (data["user"]["id_user"], data["data"]["id_variable"],
            data["data"]["chart_type"])
    return insert(query, vals)


def delete_chard_db(data: dict):
    query = "DELETE FROM dashboard_charts WHERE id_dashboard_chart = %s"
    vals = (data["data"]["id_dashboard_chart"], )
    return delete(query, vals)
