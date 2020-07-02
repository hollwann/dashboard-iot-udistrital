from oslash import Right, Left
from toolz import accumulate, assoc, reduce
from flask import jsonify
from .errors import get_error_msg
from .mysql import fetch_one


def get_props(props: list, data: dict):
    if not data and len(props) > 0:
        return Left('UD001')
    keys_exist = all(map(lambda x: x in data, props))
    if keys_exist:
        return Right(reduce(lambda x, y: assoc(x, y, data[y]), props, {}))
    return Left('UD001')


def get_auth_props(props: list, data: dict, token: str):
    if not token:
        return Left('UD006')

    data = get_props(props, data)

    query = "SELECT * FROM users WHERE token = %s"
    vals = (token,)
    user = fetch_one(query, vals).bind(lambda user: Right(
        user) if user is not None else Left('UD006'))

    return data.lift_a2(lambda data, user: {"data": data, "user": user}, user)


def either_response(data, msg=''):
    if isinstance(data, Right):
        return jsonify({'res': 200, 'msg': msg, "data": data.value})
    return jsonify({"res": data.value, "msg": get_error_msg(data.value)})
