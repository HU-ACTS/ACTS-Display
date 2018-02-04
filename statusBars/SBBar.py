## @package Default
#  SBBar module
#
#  The SBBar modules contains the SBBar class
#  It imports the TKinter based on the windows / linux version.

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image, ImageTk, ImageFilter

class SBBar():
    ## SBBar Class
    #
    #  Simple bar based status ui

    ## __init__
    #
    #  Configures config, and sets up a empty configuration file if needed
    #  @param width widow width
    #  @param height window height
    #  @param size bar size
    #  @param canvas tkinter canvas
    def __init__(self, width, height, size, canvas):
        self.width = width
        self.height = height
        self.size = size
        self.canvas = canvas
        self.barImage = None
        self.transparent = Image.open("images/transparency/background-40P.png").resize((self.width, size),Image.ANTIALIAS)

    ## update
    #
    #  bar status refresh
    #  @param state of the user
    def update(self, state):
        background = ImageTk.PhotoImage(self.transparent)
        self.barImage = background
        bck = self.canvas.create_image(0, self.height - self.size, image=background, anchor=NW, tag="goal_box")
        self.targetID = self.canvas.create_rectangle(0, self.height - self.size, self.width * (state/100), self.height, tag="trans_bar", fill="#1adb37", outline="")
