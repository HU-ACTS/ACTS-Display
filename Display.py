#!/usr/bin/env python2
## @package Default
#  Display module
#
#  The display module contains the base of the GUI.
#  The main function for the ACTS display is also contained within this module
#  Has a shebang (Unix) to call for python2 when the file executes

import sys
import UIMain, UIConfig
import DBConnector, Configuration

class Display():
    ## Display Class
    #
    #  The display class defines the display Class
    #  @var width horizontal width of the display
    #  @var hieght vertical height of the display
    width = 0
    height = 0

    ## __init__
    #
    #  Constructor of the display class
    #  Sets the width and height, Configuraion
    #  And the databasecontroller
    #  @param wd width of the the display
    #  @param ht hieght of the display
    def __init__(self, wd, ht):
        self.width  = wd
        self.height = ht
        self.conf   = Configuration.Configuraion()
        self.dbc = DBConnector.DBConnector(self.conf)
        try:
            self.dbc.configureUser()
        except:
            print("Failed to set user")

    ## displayConfig
    #
    #  Display the configuration GUI
    def displayConfig(self):
        print("Configuration mode")
        disp = UIConfig.UIConfig(self.width, self.height)
        disp.start()

    ## displayMain
    #
    #  Runs display interface with
    def displayMain(self):
        print("User mode")
        disp = UIMain.UIMain(self.width, self.height, self.conf, self.dbc)
        disp.start()

## Main functions
#
#  Initializes the program
#  Takes the config argument to show config window
if __name__ == "__main__":
    display = Display(800, 480)
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "--config"):
            display.displayConfig()
        else:
            print("Unknown parameter")
    else:
        display.displayMain()
