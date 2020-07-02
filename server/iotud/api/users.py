import functools
from flask import Blueprint, jsonify,  request
from iotud.tools import fecth_one, update, insert, get_error_msg
from string import ascii_lowercase
import random
from oslash import Right, Left
from toolz import accumulate, assoc, reduce

bp = Blueprint('users', __name__, url_prefix="/users")


@bp.route('/sign-up', methods=['POST'])
def sign_up():
    data = get_props(['name', 'email', 'password'], request.get_json())
    addedUser = data.bind(check_if_user_exists).bind(add_user_db)
    return either_response(addedUser, 'Registro completo.')


@bp.route('/login', methods=['POST'])
def login():
    data = get_props(['email', 'password'], request.get_json())
    token_generated = data.bind(append_user).bind(
        check_password).bind(generate_token)
    return either_response(token_generated, 'Login exitoso')


def get_props(props: list, data: dict):
    if not data:
        return Left('UD001')
    keys_exist = all(map(lambda x: x in data, props))
    if keys_exist:
        return Right(reduce(lambda x, y: assoc(x, y, data[y]), props, {}))
    return Left('UD001')


def either_response(data, msg=''):
    if isinstance(data, Right):
        return jsonify({'res': 200, 'msg': msg, "data": data.value})
    return jsonify({"res": data.value, "msg": get_error_msg(data.value)})


def add_user_db(user: dict):
    query = "INSERT INTO users(name, email, password, id_rol) \
            VALUES (%s, %s, %s, %s)"
    vals = (user['name'],
            user['email'],
            user['password'],
            1)
    return insert(query, vals)


def check_if_user_exists(data: dict):
    query = "SELECT * FROM users WHERE email = %s"
    vals = (data['email'],)
    return fecth_one(query, vals).bind(
        lambda user: Right(data) if user is None else Left('UD002'))


def append_user(data: dict):
    query = "SELECT * FROM users WHERE email = %s"
    vals = (data['email'],)
    return fecth_one(query, vals).bind(
        lambda user: Left('UD003') if user is None else Right({"user": user, "body": data}))


def check_password(data):
    if data['user']['password'] == data['body']['password']:
        return Right(data["user"])
    return Left('UD004')


def generate_token(user: dict):
    token = ''.join(random.choice(ascii_lowercase) for i in range(32))
    query = "UPDATE users SET token = %s WHERE email = %s"
    vals = (token, user['email'])
    return update(query, vals).map(lambda _: {"token": token})
