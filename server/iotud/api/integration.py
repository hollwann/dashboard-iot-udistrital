from datetime import datetime
from flask import Blueprint, request
from iotud.tools import fetch_one, insert, either_response, auth_device_write
from oslash import Right, Left
import json
from dateutil.parser import parse

bp = Blueprint('integration', __name__, url_prefix="/api")


@bp.route('/write_data', methods=['POST'])
def write_data():
    data = auth_device_write(['payload_fields', 'metadata'],
                             request.get_json(),
                             request.headers.get('Authorization'))
    # check ownership
    data_checked_owner = data.bind(check_ownership)
    # check datatype
    data_checked_data = data_checked_owner.bind(check_data)
    addedData = data_checked_data.bind(write_data_db)
    return either_response(addedData, 'Datos guardados con éxito')


def check_ownership(data: dict):
    variables_data = data["data"]["payload_fields"]["data"]
    device = data["device"]
    for variable in variables_data:
        print(variable)
        isOwner = check_variable_ownership(
            device["api_key_write"], variable["id"])
        if not isinstance(isOwner, Right):
            return Left('UD006')
    return Right(data)


def check_data(data: dict):
    try:
        variables_data = data["data"]["payload_fields"]["data"]
        for variable in variables_data:
            variable_db = get_variable_db(variable["id"]).value
            if variable_db["id_variable_type"] == 1:
                float(variable["value"])
            elif variable_db["id_variable_type"] == 2:
                coords = variable["value"]
                if len(coords) != 2:
                    raise  Exception('')
                float(coords[0])
                float(coords[1])
            else:
                json.loads(variable["value"])
        return Right(data)
    except Exception as e:
        return Left('UD007')


def get_variable_db(id: str):
    query = "SELECT * FROM variables WHERE id_variable = %s"
    vals = (id,)
    variable = fetch_one(query, vals)
    return variable


def write_data_db(data: dict):
    variables_data = data["data"]["payload_fields"]["data"]
    metadata = data["data"]["metadata"]
    meta_info = data["data"]["meta_info"]
    for variable in variables_data:
        written_data = write_variable_data(variable, meta_info, metadata)
        if not isinstance(write_data, Right):
            return written_data
    return Right(True)


def check_variable_ownership(api_key, id_variable):
    query = "SELECT * FROM variables \
            INNER JOIN devices ON devices.id_device = variables.id_device \
            WHERE devices.api_key_write = %s AND variables.id_variable = %s"
    vals = (api_key, id_variable, )
    variable = fetch_one(query, vals)
    return variable.bind(lambda variable: Left('UD006') if variable is None else Right(variable))


def write_variable_data(variable_data, meta_info, metadata):
    try:
        query = "INSERT INTO variable_data(id_variable, value, timestamp_data, timestamp_gateway, timestamp_ttn, meta_info, latitude, longitude, altitude)  \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        vals = (
            variable_data["id"],
            str(variable_data["value"]),
            datetime.fromtimestamp(variable_data["timestamp"]),
            parse(metadata["gateways"][0]['time']),
            parse(metadata['time']),
            meta_info,
            metadata['latitude'],
            metadata['longitude'],
            metadata['altitude'])
        return insert(query, vals)
    except Exception as e:
        print(e)
        return Left('UD001')
