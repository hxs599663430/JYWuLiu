
import pymysql

from common.db_pool import get_db_pool


class BaseSelect(object):
    def __init__(self):
        self.conn = get_db_pool()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def select_all(self, sql, values=None):
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        self.cursor.close()
        self.conn.close()
        return self.cursor.fetchall()

    def select_one(self, sql, values=None):
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchone()
