## @package Default
#  UIConfig module
#
#  User interface for Configuration
#  Switches Tkinter depending on platform
try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    from tkinter.ttk import *
import os
from os.path import basename

class UIConfig():
    ## UIConfig Class
    #
    #  The display class defines the display Class
    #  @var width horizontal width of the display
    #  @var hieght vertical height of the display

    ## __init__
    #
    #  constructor for the UI configuration window
    #  @param width window width
    #  @param height window height
    def __init__(self, width, height):
        self.state = 0
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.attributes('-fullscreen', True)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)

    ## display
    #
    #  Display the window
    def display(self, offset=30):
        #self.canvas.delete('all')
        self.box_value = StringVar()
        self.box = Combobox(self.root, textvariable=self.box_value)
        self.box.bind("<<ComboboxSelected>>", self.newselection)

        backgrounds = []
        for background in os.listdir('images/'):
            backgrounds.append(os.path.splitext('images/' + background)[0])

        self.box['values'] = backgrounds
        self.box.current(0)
        self.box.grid(column=0, row=0)
        #self.canvas.pack()
        self.root.after(1000, self.display)

    ## newselection
    #
    #  select update
    def newselection(self, event):
        self.value_of_combo = self.box.get()
        print(self.value_of_combo)

    ## start
    #
    #  run display config
    def start(self):
        self.display()
        self.root.mainloop()
