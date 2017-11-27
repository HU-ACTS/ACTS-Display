import MySQLdb

class DBConnector:
    def __init__(self, conf):
        self.config = conf
        self.connect

    def connect(self):
        conf = self.config
        self.db = MySQLdb.connect(
            host=conf.host,    # your host, usually localhost
            user=conf.user,         # your username
            passwd=conf.password,       # your password
            db=conf.db              # name of the data base
        )
        self.cur = self.db.cursor()

    def poll(self):
        # Use all the SQL you like
        self.cur.execute("SELECT GOAL FROM ACTS.USERS WHERE user=1")

        # print all the first cell of all the rows
        for row in self.cur.fetchall():
            print(row[0])

    def configureUser(self):
        self.connect()
        self.cur.execute("SELECT * FROM ACTS.USERS WHERE user=1")
        user, goal, image = self.cur.fetchall()[0]
        self.config.setUser(user, goal, image)

    def close(self):
        self.db.close()
