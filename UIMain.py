try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import time
from datetime import datetime
import Configuration as conf

class UIMain():
    targetID  = 0
    nameID    = 0
    timeID    = 0
    dateID    = 0
    happyID   = 0
    okID      = 0
    unhappyID = 0
    sphereOneID     = 0
    sphereTwoID     = 0
    sphereThreeID   = 0
    sphereFourID    = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.attributes('-fullscreen', True)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)

    def drawBall(self, x, y, size, fill=100):
        radius =  size / 2
        filler = radius * float(fill / 100.0)
        xposTop = x + ( radius )
        yposTop = y + ( radius )
        xposBottom = x - ( radius )
        yposBottom = y - ( radius )

        # Underlaying oval
        self.canvas.create_oval(xposTop, yposTop, xposBottom, yposBottom, fill="grey", stipple='gray75', outline="black", width=2)

        # Completion oval
        xposTop = x + ( filler )
        yposTop = y + ( filler )
        xposBottom = x - ( filler )
        yposBottom = y - ( filler )
        self.canvas.create_oval(xposTop, yposTop, xposBottom, yposBottom, fill="#1adb37", outline="")

    def setDateTime(self, date, time):
        dt = datetime.now()
        self.canvas.itemconfig(date, text=("" + str(dt.day) + " " + conf.months[dt.month]))
        if dt.minute < 10:
            minutes = str("0" + str(dt.minute))
        else:
            minutes = str(dt.minute)
        self.canvas.itemconfig(date, text=("" + str(dt.hour) + ":" + minutes))
        self.root.after(30000, lambda: self.setDateTime(date, time))

    def displayStateBalls(self, height, offset, state, count):
        if count > 100:
            count = 100
        border = self.width - (offset *2)
        size = ( border / count ) - offset


        segment_state = 0
        segment_size = 100 / count
        for segment in range(0, count):
            a = state - (segment_size * (segment + 1))
            if a <= 0:
                segment_state = 0
            else:
                segment_state = (a/(segment_size * (segment + 1))) * 100
            self.drawBall((offset + (size / 2)) + ( (size + offset ) * segment), height, size, segment_state)

    def crossfade(self, state):
        state = 90
        im = Image.open("images/forest-1.jpg").resize((self.width, self.height), Image.ANTIALIAS)
        im = im.filter(ImageFilter.GaussianBlur(3))
        im = im.crop( ( self.width - (self.width * (state/100)), 0, self.width, self.height) )
        ima = ImageTk.PhotoImage(im)
        idt = self.canvas.create_image(self.width, 0, image=ima, anchor=NE)


    def display(self, offset=30):
        image = Image.open("images/forest-1.jpg").resize((self.width, self.height),Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(image)

        self.crossfade(10)

        self.targetID = self.canvas.create_text(int(abs(self.width / 2)), offset + 20, justify=CENTER, text="Ik wil dit werkend krijgen! :) echt ik wil dit zo graag werkend hebben", width=self.width, fill="white", font=("Helvetica", 30), anchor=CENTER)
        box = self.canvas.bbox(self.targetID)
        bck40 = Image.open("images/transparency/background-20P.png").resize((box[2], box[3]),Image.ANTIALIAS)
        bck40_img = ImageTk.PhotoImage(bck40)
        bck = self.canvas.create_image(int(abs(self.width / 2)),offset + 20, image=bck40_img, anchor=CENTER)
        self.canvas.lower(bck)

        self.timeID = self.canvas.create_text(int(abs(self.width / 2)), offset + 170, text="11:00", fill="white", font=("Helvetica", 70), anchor=CENTER)
        self.dateID = self.canvas.create_text(int(abs(self.width / 2)), offset + 240, text="9 November", fill="white", font=("Helvetica", 30), anchor=CENTER)

        background_s = self.canvas.create_image(0,0, image=background_image, anchor=NW)

        self.canvas.lower(background_s)
        self.setDateTime(self.timeID, self.dateID)
        #self.displayStateBalls(340, 5, 50, 10)
        self.canvas.pack()
        self.root.mainloop()
