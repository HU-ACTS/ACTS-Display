try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import SBBar, SBCrossfade

class SBBarfade():
    def __init__(self, image, width, height, size, canvas):
        self.bar =  SBBar.SBBar(width, height, size, canvas)
        self.fade = SBCrossfade.SBCrossfade(image, width, height, canvas)

    def update(self, state):
        self.bar.update(state)
        self.fade.update(state)
