try:
    import configparser as config
except ImportError:
    import ConfigParser as config
import os

class Configuraion():
    def __init__(self):
        self.config = config.ConfigParser()
        if os.path.exists("acts.cfg"):
            self.config.read("acts.cfg")
        else:
            # Creating default configuration file
            def_months = ["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december"]
            self.config.add_section('System')
            self.config.set('System', 'id', 0)
            self.config.set('System', 'bar', 0)
            self.config.set('System', 'image', 1)
            self.config.set('System', 'goal', 'Wat wil ik bereiken')
            self.config.set('System', 'months', def_months)
            self.config.add_section('Database')
            self.config.set('Database', 'host', '192.168.1.102')
            self.config.set('Database', 'db', 'ACTS')
            self.config.set('Database', 'user', 'getter')
            self.config.set('Database', 'password', 'test')

            # Writing our configuration file to 'example.cfg'
            with open('acts.cfg', 'wb') as configfile:
                self.config.write(configfile)
        self.readConf()

    ## setUser
    #   Sets requisted user data
    def setUser(self, id, goal, image):
        self.config.set('System', 'id', id)
        self.config.set('System', 'image', image)
        self.config.set('System', 'goal', goal)
        with open('acts.cfg', 'wb') as configfile:
            self.config.write(configfile)

    ## readConf
    #   Reads configuration
    def readConf(self):
        self.config.sections()
        self.config.read("acts.cfg")

        self.months = self.config.get('System', 'months')
        self.bar    = self.config.getint('System', 'bar')
        self.id     = self.config.getint('System', 'id')
        self.goal   = self.config.get('System', 'goal')

        self.host   = self.config.get('Database', 'host')
        self.db     = self.config.get('Database', 'db')
        self.user   = self.config.get('Database', 'user')
        self.password = self.config.get('Database', 'password')
        print(self.months)
