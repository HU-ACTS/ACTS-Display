import MySQLdb

class DBConnector:
    def __init__(self, conf):
        self.config = conf
        self.connect

    def connect(self):
        conf = self.config
        db = MySQLdb.connect(
            host=conf.host,    # your host, usually localhost
            user=conf.user,         # your username
            passwd=conf.password,       # your password
            db=conf.db              # name of the data base
        )
        return db

    def poll(self):
        result = 1
        target = 1
        with self.connect() as cur:
            # Use all the SQL you like
            cur.execute("SELECT RESULTS.result, GOALS.goal FROM RESULTS, GOALS where RESULTS.user=1 and GOALS.user=1 LIMIT 1")
            result, target = cur.fetchall()[0]
        return (result / float(target)) * 100

    def configureUser(self):
        with self.connect() as cur:
            cur.execute("SELECT * FROM ACTS.USERS WHERE user=1")
            user, goal, image, bar = cur.fetchall()[0]
            self.config.setUser(user, goal, image, bar)
