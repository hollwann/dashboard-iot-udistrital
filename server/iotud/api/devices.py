import functools
from datetime import datetime
from flask import Blueprint, jsonify,  request
from iotud.tools import fetch_all, fetch_one, update, insert, get_auth_props, either_response, delete
from string import ascii_lowercase
import random
from oslash import Right, Left
from toolz import accumulate, assoc, reduce


bp = Blueprint('devices', __name__, url_prefix="/users")


@bp.route('/create_device', methods=['POST'])
def create_device():
    data = get_auth_props(['name', 'description'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    addedDevice = data.bind(add_device_db)
    return either_response(addedDevice, 'Dispositivo creado con exito.')


@bp.route('/delete_device', methods=['POST'])
def delete_device():
    data = get_auth_props(['id_device'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    deletedDevice = data.bind(check_device_ownership).bind(delete_device_db)
    return either_response(deletedDevice, 'Dispositivo eliminado con exito.')


@bp.route('/update_device', methods=['POST'])
def update_device():
    data = get_auth_props(['id_device', 'name', 'description'],
                          request.get_json(),
                          request.headers.get('Authorization'))
    updatedDevice = data.bind(check_device_ownership).bind(update_device_db)
    return either_response(updatedDevice, 'Dispositivo actualizado con exito.')


@bp.route('/get_devices', methods=['GET'])
def get_devices():
    data = get_auth_props([],
                          request.get_json(),
                          request.headers.get('Authorization'))
    devices = data.bind(get_devices_db)
    return either_response(devices)


def check_device_ownership(data: dict):
    query = "SELECT * FROM devices WHERE id_device = %s AND id_user = %s"
    vals = (data["data"]["id_device"], data["user"]["id_user"])
    device = fetch_one(query, vals)
    return device.bind(lambda device: Left('UD006') if device is None else Right(data))


def get_devices_db(data: dict):
    query = "SELECT * FROM devices WHERE id_user = %s"
    vals = (data["user"]["id_user"],)
    devices = fetch_all(query, vals)
    return devices


def add_device_db(data: dict):
    query = "INSERT INTO devices(name, description, variables_number,\
             api_key_read, api_key_write, timestamp, id_user)\
            VALUES (%s, %s, %s, %s, %s, %s, %s)"
    vals = (data["data"]["name"], data["data"]["description"], 0,
            gen_apikey(),gen_apikey(), datetime.now(), data["user"]["id_user"])
    return insert(query, vals)


def update_device_db(data: dict):
    query = "UPDATE devices SET name = %s, description = %s \
            WHERE id_device = %s"
    vals = (data["data"]["name"], data["data"]
            ["description"], data["data"]["id_device"])
    return update(query, vals)


def delete_device_db(data: dict):
    query = "DELETE FROM devices WHERE id_device = %s"
    vals = (data["data"]["id_device"], )
    return delete(query, vals)


def gen_apikey():
    apikey = ''.join(random.choice(ascii_lowercase) for i in range(32))
    return apikey
