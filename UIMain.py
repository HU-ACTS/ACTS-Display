try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import time
from datetime import datetime
import Configuration as conf
import sys
sys.path.append('statusBars/')
import SBSpheres, SBCrossfade
import DBConnector
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
    running = True

    def __init__(self, width, height, statusStyle, conf, dbc):
        self.state = 0
        self.width = width
        self.height = height
        self.configuration = conf
        self.database = dbc
        self.root = Tk()
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.attributes('-fullscreen', True)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.background = Image.open("images/forest-1.jpg").resize((self.width, self.height),Image.ANTIALIAS)
        self.transparent = Image.open("images/transparency/background-20P.png").resize((self.width, self.height),Image.ANTIALIAS)
        self.background_image = None
        self.tmptrans = None
        self.setStatus(self.configuration.bar)

    def setStatus(self, statusStyle):
        if statusStyle == 0:
            self.statusBar = SBSpheres.SBSpheres(400, 50, 6, self.width, self.height, self.canvas)
        elif statusStyle == 1:
            self.statusBar = SBCrossfade.SBCrossfade(self.background, self.width, self.height, self.canvas)
        elif statusStyle == 2:
            pass
        else:
            self.statusBar = SBSpheres.SBSpheres(340, 20, 10, self.width, self.height, self.canvas)

    def setDateTime(self, date, time):
        dt = datetime.now()
        self.canvas.itemconfig(date, text=("" + str(dt.day) + " " + self.configuration.months[dt.month]))
        if dt.minute < 10:
            minutes = str("0" + str(dt.minute))
        else:
            minutes = str(dt.minute)
        if dt.hour < 10:
            hour = str(" " + str(dt.hour))
        else:
            hour = str(dt.hour)
        self.canvas.itemconfig(date, text=("" + str(dt.hour) + ":" + minutes))
        #self.root.after(30000, lambda: self.setDateTime(date, time))

    def drawGoal(self, offset):
        self.targetID = self.canvas.create_text(int(abs(self.width / 2)), offset + 20, justify=CENTER, tag="goal", text="Ik wil dit werkend krijgen! :) echt ik wil dit zo graag werkend hebben", width=self.width, fill="white", font=("Helvetica", 30), anchor=CENTER)
        box = self.canvas.bbox(self.targetID)
        bck40 = self.transparent.resize((box[2], box[3]),Image.ANTIALIAS)
        bck40_img = ImageTk.PhotoImage(bck40)
        self.tmptrans = bck40_img
        bck = self.canvas.create_image(int(abs(self.width / 2)),offset + 20, image=bck40_img, anchor=CENTER, tag="goal_box")
        self.canvas.lower("goal_box")
        self.canvas.pack()

    ## Display
    #   Display function, set background and adds
    def display(self, offset=30):
        # Clear and reload
        self.canvas.delete('all')
        self.background_image = ImageTk.PhotoImage(self.background)

        # Redraw
        self.drawGoal(offset)
        self.timeID = self.canvas.create_text(int(abs(self.width / 2)), offset + 170, text="11:00", fill="white", font=("Helvetica", 70), anchor=CENTER)
        self.dateID = self.canvas.create_text(int(abs(self.width / 2)), offset + 240, text="9 November", fill="white", font=("Helvetica", 30), anchor=CENTER)

        # Update information
        self.database.poll()

        self.statusBar.update(45)
        self.setDateTime(self.timeID, self.dateID)

        # Set the background image
        background_s = self.canvas.create_image(0,0, image=self.background_image, anchor=NW)

        # Lower the background image to the back
        self.canvas.lower(background_s)

        #self.displayStateBalls(340, 5, 50, 10)
        self.canvas.pack()
        self.state += 0.1
        #self.root.quit()
        # Updater
        if self.running:
            self.root.after(1000, self.display)
        else:
            self.root.quit()

    def stop(self):
        print("stopping main window")
        self.running = False
        self.root.quit()

    def start(self):
        self.display()
        self.root.mainloop()
