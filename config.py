import mysql.connector

db = ("localhost", "3307", "root", "", "dental_appointment_booking_system")
class config_sql:
    def __init__(self):
        self._conn =  mysql.connector.connect(host=db[0], port=db[1], user=db[2], password=db[3],
                                           database=db[4])
        self._cursor = self._conn.cursor()

    def _getrow(self):
        self.rowscount = self._cursor.rowcount
        self._cursor.close()
        self._conn.close()
        return self.rowscount

    def _selectall(self, sql, args=None):
        self._cursor.execute(sql, args)
        self.sel = self._cursor.fetchall()
        return self.sel

    def _selectone(self, sql, args=None):
        self._cursor.execute(sql, args)
        self.sel = self._cursor.fetchone()
        return self.sel

    def _insert(self, sql, args=None):
        self.ins = self._cursor.executemany(sql, args)
        return self.ins

    def _update(self,sql, args=None):
        self.upd = self.cur.executemany(sql,args)
        return self.upd

    def _delete(self, sql, args=None):
        self.delete = self.cur.executemany(sql,args)
        return self.delete