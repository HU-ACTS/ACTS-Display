try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import SBBar

class SBCrossfade():

    def __init__(self, image, width, height, canvas):
        self.image = image
        self.width = width
        self.height = height
        self.canvas = canvas
        self.fadeImage = None
        self.bar = None

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

    def setImage(self, image):
        self.image = image
