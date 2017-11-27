#!/usr/bin/env python2
import sys
import UIMain, UIConfig
import DBConnector, Configuration
class Display():
    width = 0
    height = 0

    def __init__(self, wd, ht):
        self.width  = wd
        self.height = ht
        self.conf   = Configuration.Configuraion()
    def displayConfig(self):
        print("Configuration mode")
        disp = UIConfig.UIConfig(self.width, self.height)
        disp.start()

    def displayMain(self):
        dbc = DBConnector.DBConnector(self.conf)
        dbc.configureUser()
        disp = UIMain.UIMain(self.width, self.height, 0, self.conf, dbc)
        disp.start()

if __name__ == "__main__":
    display = Display(800, 480)
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "--config"):
            display.displayConfig()
        else:
            print("Unknown parameter")
    else:
        display.displayMain()
