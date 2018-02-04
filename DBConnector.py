## @package Default
#  DBConnector module
#
#  Database connector module uses the python mysqld module
import MySQLdb

class DBConnector:
    ## Display Class
    #
    #  The databasecontroller performs the data requests to teh server

    ## __init__
    #
    #  Constructor of the databasecontroller class
    #  @param conf configuration where login details can be loaded from
    def __init__(self, conf):
        self.config = conf

    ## connect
    #
    #  connect to the maria database with the lofin credentials
    def connect(self):
        conf = self.config
        db = MySQLdb.connect(
            host=conf.host,    # your host, usually localhost
            user=conf.user,         # your username
            passwd=conf.password,       # your password
            db=conf.db              # name of the data base
        )
        return db

    ## poll
    #
    #  Poll the database and calculates the completed precentage
    def poll(self):
        result = -1
        target = -1
        with self.connect() as cur:
            # Use all the SQL you like
            cur.execute("SELECT SUM(Value) FROM Result where UserId="+str(self.conf.id)+" and Date=CURRENT_DATE")
            result = cur.fetchone()[0]
            cur.execute("SELECT Value FROM Target where UserId="+str(self.conf.id)+" and Date=CURRENT_DATE limit 1")
            target = cur.fetchone()[0]
        if( target == -1):
            return 0
        else:
            return (result / float(target)) * 100.0

    ## configureUser
    #
    #  Configure the user data by requesting it from the database
    def configureUser(self):
        with self.connect() as cur:
            cur.execute("SELECT UserId, `Key`, Bar, Background, MotoText FROM User WHERE User.UserId="+str(self.config.id))
            user, key, bar, image, goal = cur.fetchall()[0]
            self.config.setUser(user, goal, image, bar, key)
