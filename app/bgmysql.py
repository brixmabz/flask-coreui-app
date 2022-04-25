# General mysql connector file

# bgr Github Version 0.0.12 Are Casilla 20190315 -> 20191004
# bgmysql.py and config.py master file is in DevExtern/p2-are

# https://flask.palletsprojects.com/en/1.0.x/tutorial/database/  LEARN
# https://stackoverflow.com/questions/15083967/when-should-flask-g-be-used
# https://speakerdeck.com/mitsuhiko/advanced-flask-patterns-1?slide=20

import pymysql.cursors
import os
import ast
# pip install python-dotenv
from dotenv import load_dotenv
from sqlalchemy import false

load_dotenv()


mydbhost = os.getenv("DB_HOST")
mydbport = int(os.getenv("DB_PORT"))
mydbname = os.getenv("DB_DATABASE")
mydbuser = os.getenv("DB_USERNAME")
mydbpass = os.getenv("DB_PASSWORD")

cnx = pymysql.connect(
    host=mydbhost,
    port=mydbport,
    db=mydbname,
    user=mydbuser,
    passwd=mydbpass,
    autocommit=False,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,  # Dict is simpler than tuple
    connect_timeout=15
)


def sql_exec(cur2, sql, param=None, commit=False):
    """Used to execute MySQL statements. We try to execute SQL via this function. This enfore things like cnx.ping
       Usage example: bgmysql.sql_exec(cur, sql, commit = True)"""
    # https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.ping
    # ping(reconnect=True) Check if the server is alive. Connection will timeout if we do not use this
    cnx.ping(True)

    if not param:
        ret = cur2.execute(sql)
    else:
        ret = cur2.execute(sql, param)
    if commit is True:
        cnx.commit()
    return ret


def sql_exec_commit(cur2, sql, param=None):
    """
        Used to execute MySQL statements and commit. We try to execute SQL via this function.
        This enforce things like cnx.ping
        Usage example: bgmysql.sql_exec(cur, sql)
    """
    # https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.ping
    # ping(reconnect=True) Check if the server is alive. Connection will timeout if we do not use this
    cnx.ping(True)

    if not param:
        ret = cur2.execute(sql)
    else:
        ret = cur2.execute(sql, param)

    cnx.commit()
    ret = cur2.lastrowid

    return ret


if __name__ == '__main__':
    pass
    # execute_mysql()