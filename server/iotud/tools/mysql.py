import mysql.connector
from oslash import Right, Left


def get_cnx():
    cnx = mysql.connector.connect(user='root', password='UsaCnsc-2019',
                                  host='localhost', database='dashboard_ud',
                                  auth_plugin='mysql_native_password',
                                  use_pure=True)
    cursor = cnx.cursor(dictionary=True)
    return cnx, cursor


def query_wrapper(query: str, vals: tuple, f):
    try:
        cnx, cursor = get_cnx()
        cursor.execute(query, vals)
        result = f(cnx, cursor)
        cnx.close()
        return Right(result)
    except:
        return Left('UD005')


def insert(query: str, vals: tuple):
    def insert_function(cnx, cursor):
        cnx.commit()
        return cursor.lastrowid
    return query_wrapper(query, vals, insert_function)


def fecth_one(query: str, vals: tuple):
    def fetch_one_function(cnx, cursor):
        return cursor.fetchone()
    return query_wrapper(query, vals, fetch_one_function)


def update(query: str, vals: tuple):
    def update_function(cnx, cursor):
        cnx.commit()
        return cursor.lastrowid
    return query_wrapper(query, vals, update_function)
