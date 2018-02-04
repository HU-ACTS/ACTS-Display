## @package Default
#  Configuration module
#
#  The configuration modules contains the configuration loader for the display
#  It imports the configparser based on the windows / linux version.
try:
    import configparser as config
except ImportError:
    import ConfigParser as config
import os

class Configuraion():
    ## Configuration Class
    #
    #  Loads the configuration and makes it available
    #  to the rest of the program.

    ## __init__
    #
    #  Configures config, and sets up a empty configuration file if needed
    def __init__(self):
        self.config = config.ConfigParser()
        if os.path.exists("acts.cfg"):
            self.config.read("acts.cfg")
        else:
            # Creating default configuration file
            def_months = ["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december"]
            self.config.add_section('System')
            self.config.set('System', 'id', 0)
            self.config.set('System', 'key', None)
            self.config.set('System', 'bar', 0)
            self.config.set('System', 'image', "forest-1.jpg")
            self.config.set('System', 'goal', 'Wat wil ik bereiken')
            self.config.set('System', 'months', def_months)
            self.config.add_section('Database')
            self.config.set('Database', 'host', 'acts.cl7lb3l0h8d5.eu-central-1.rds.amazonaws.com')
            self.config.set('Database', 'db', 'acts_maria')
            self.config.set('Database', 'user', 'getter')
            self.config.set('Database', 'password', 'test')

            # Writing our configuration file to 'example.cfg'
            with open('acts.cfg', 'wb') as configfile:
                self.config.write(configfile)

        self.readConf()

    ## setUser
    #
    #   Sets requisted user data
    #   @param id user id
    #   @param goal set's moto text
    #   @param image file name
    #   @param bar bar style
    #   @param key for indentification
    def setUser(self, id, goal, image, bar, key):
        self.config.set('System', 'id', id)
        self.config.set('System', 'key', key)
        self.config.set('System', 'image', image)
        self.config.set('System', 'goal', goal)
        self.config.set('System', 'bar', bar)
        with open('acts.cfg', 'wb') as configfile:
            self.config.write(configfile)

    ## readConf
    #
    #   Reads configuration
    def readConf(self):
        self.config.sections()
        self.config.read("acts.cfg")

        self.months = self.config.get('System', 'months')
        self.bar    = self.config.getint('System', 'bar')
        self.id     = self.config.getint('System', 'id')
        self.key    = self.config.get('System', 'key')
        self.goal   = self.config.get('System', 'goal')
        self.image  = self.config.get('System', 'image')

        self.host   = self.config.get('Database', 'host')
        self.db     = self.config.get('Database', 'db')
        self.user   = self.config.get('Database', 'user')
        self.password = self.config.get('Database', 'password')
        print(self.months)
