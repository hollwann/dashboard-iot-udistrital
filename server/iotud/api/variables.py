import functools
from datetime import datetime
from flask import Blueprint, jsonify,  request
from iotud.tools import fetch_all, fetch_one, update, insert, get_auth_props, either_response, delete
from iotud.api.devices import check_device_ownership
from string import ascii_lowercase
import random
from oslash import Right, Left
from toolz import accumulate, assoc, reduce


bp = Blueprint('variables', __name__, url_prefix="/users")


@bp.route('/create_variable', methods=['POST'])
def create_variable():
    data = get_auth_props(['name', 'id_device', 'id_variable_type'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    addedVariable = data.bind(check_device_ownership).bind(add_variable_db)
    return either_response(addedVariable, 'Variable creado con exito.')


@bp.route('/delete_variable', methods=['POST'])
def delete_variable():
    data = get_auth_props(['id_variable'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    deletedVariable = data.bind(
        check_ownership_variable).bind(delete_variable_db)
    return either_response(deletedVariable, 'Dispositivo eliminado con exito.')


@bp.route('/get_variables', methods=['POST'])
def get_devices():
    data = get_auth_props(['id_device'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    variables = data.bind(check_device_ownership).bind(get_variables_db)
    return either_response(variables)


def check_ownership_variable(data: dict):
    query = "SELECT * FROM variables \
            INNER JOIN devices ON devices.id_device = variables.id_device \
            WHERE devices.id_user = %s AND variables.id_variable = %s"
    vals = (data["user"]["id_user"], data["data"]["id_variable"], )
    device = fetch_one(query, vals)
    return device.bind(lambda device: Left('UD006') if device is None else Right(data))


def delete_variable_db(data: dict):
    query = "DELETE FROM variables WHERE id_variable = %s"
    vals = (data["data"]["id_variable"], )
    return delete(query, vals)


def add_variable_db(data: dict):
    query = "INSERT INTO variables(name, id_device, id_variable_type) VALUES (%s, %s, %s)"
    vals = (data["data"]["name"], data["data"]
            ["id_device"], data["data"]["id_variable_type"])
    return insert(query, vals)


def get_variables_db(data: dict):
    query = "SELECT * FROM variables WHERE id_device = %s"
    vals = (data["data"]["id_device"],)
    variables = fetch_all(query, vals)
    return variables
