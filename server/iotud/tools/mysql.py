import mysql.connector
from oslash import Right, Left


def get_cnx():
    cnx = mysql.connector.connect(user='root', password='Thegitud2020',
                                  host='localhost', database='dashboard_ud',
                                  auth_plugin='mysql_native_password',
                                  use_pure=True)
    cursor = cnx.cursor(dictionary=True)
    return cnx, cursor


def insert(query: str, vals: tuple):
    return _query_wrapper(query, vals, _commit)


def fetch_one(query: str, vals: tuple):
    def fetch_one_function(cnx, cursor):
        return cursor.fetchone()
    return _query_wrapper(query, vals, fetch_one_function)


def fetch_all(query: str, vals: tuple):
    def fetch_all_function(cnx, cursor):
        return cursor.fetchall()
    return _query_wrapper(query, vals, fetch_all_function)


def update(query: str, vals: tuple):
    return _query_wrapper(query, vals, _commit)


def delete(query: str, vals: tuple):
    return _query_wrapper(query, vals, _commit)


def _commit(cnx, cursor):
    cnx.commit()
    return {"id": cursor.lastrowid}


def _query_wrapper(query: str, vals: tuple, f):
    try:
        cnx, cursor = get_cnx()
        cursor.execute(query, vals)
        result = f(cnx, cursor)
        cnx.close()
        return Right(result)
    except Exception as e:
        print(str(e))
        return Left('UD005')
