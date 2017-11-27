try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    from tkinter.ttk import *
import os
from os.path import basename

class UIConfig():
    def __init__(self, width, height):
        self.state = 0
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.attributes('-fullscreen', True)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)

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

    def newselection(self, event):
        self.value_of_combo = self.box.get()
        print(self.value_of_combo)

    def start(self):
        self.display()
        self.root.mainloop()
