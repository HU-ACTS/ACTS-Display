import MySQLdb

class DBConnector:
    def __init__(conf):
        self.db = MySQLdb.connect(
            host=conf.localhost,    # your host, usually localhost
            user=conf.user,         # your username
            passwd=conf.pasw,       # your password
            db=conf.db              # name of the data base
        )
        self.cur = db.cursor()
    def poll():
        # Use all the SQL you like
        cur.execute("SELECT * FROM YOUR_TABLE_NAME")

        # print all the first cell of all the rows
        for row in cur.fetchall():
            print row[0]
    def close():
        db.close()
