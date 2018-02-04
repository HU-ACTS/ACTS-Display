## @package Default
#  Configuration module
#
#  The SBBarfade module contains the SBBarfade class
#  It imports the TKinter based on the windows / linux version.
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import SBBar, SBCrossfade

class SBBarfade():
    ## SBBarfade Class
    #
    #  Combination between Bar status display and background fade state display

    ## __init__
    #
    #  COnfigures bar fade
    #  @param image background image
    #  @param width window width
    #  @param height window height
    #  @param size bar size
    #  @param canvas tkinter window canvas
    def __init__(self, image, width, height, size, canvas):
        self.bar =  SBBar.SBBar(width, height, size, canvas)
        self.fade = SBCrossfade.SBCrossfade(image, width, height, canvas)

    ## update
    #
    #  barfade status refresh
    #  @param state of the user
    def update(self, state):
        self.bar.update(state)
        self.fade.update(state)
