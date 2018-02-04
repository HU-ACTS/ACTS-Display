## @package Default
#  Configuration module
#
#  SBCrossfade module is part of the graphical modules for status display
#  Uses try import to select the correct module for the platform
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import SBBar

class SBCrossfade():
    ## Configuration Class
    #
    #  SBCrossfade blurs the background image depending on status

    ## __init__
    #
    #  Init setsup the positional argumnts of the blur(fade) based UI
    #  @param image background image
    #  @param width widow width
    #  @param height window height
    #  @param canvas tkinter canvas
    def __init__(self, image, width, height, canvas):
        self.image = image
        self.width = width
        self.height = height
        self.canvas = canvas
        self.fadeImage = None
        self.bar = None

    ## update
    #
    #  fade status refresh
    #  @param state of the user
    def update(self, state):
        # Prevent overcompletion
        if state > 100:
            state = 100
        #Create faded cropped image with GaussianBlur
        fade = self.image.filter(ImageFilter.GaussianBlur(3))
        fade = fade.crop( ( self.width * (state/100), 0, self.width, self.height) )
        fade = ImageTk.PhotoImage(fade)
        self.fadeImage = fade
        filterImage = self.canvas.create_image(self.width, 0, image=fade, anchor=NE)
        self.canvas.lower(filterImage)

    ## setImage
    #
    #  Set the image
    #  sets the image for background
    def setImage(self, image):
        self.image = image
