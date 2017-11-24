#!/usr/bin/env python
import sys
import UIMain
import UIConfig
class Display():
    width = 0
    height = 0

    def __init__(self, wd, ht):
        self.width = wd
        self.height = ht

    def displayConfig(self):
        print("Configuraion mode")
        disp = UIConfig.UIConfig(self.width, self.height)
        disp.display()

    def displayMain(self):
        disp = UIMain.UIMain(self.width, self.height)
        disp.display()

if __name__ == "__main__":
    display = Display(800, 480)
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "--config"):
            display.config()
        else:
            print("Unknown parameter")
    else:
        display.displayMain()
