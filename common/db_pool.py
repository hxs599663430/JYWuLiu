import pymysql
from DBUtils.PooledDB import PooledDB

import config


def get_db_pool():
    db_pool = PooledDB(
        pymysql,
        5,
        host=config.MYSQL_HOST,
        port=config.MYSQL_PORT,
        user=config.MYSQL_USER,
        passwd=config.MYSQL_PASSWORD,
        db=config.MYSQL_DB,
        charset=config.MYSQL_CHARTSET
    )
    return db_pool
