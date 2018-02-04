## @package Default
#  UIMain module
#
#  The UIMain module defines
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
import SBSpheres, SBCrossfade, SBBar, SBBarfade
import DBConnector

class UIMain():
    ## UIMain Class
    #
    #  The UIMain class defines the main user interface Class
    #  @var targetID target id
    #  @var nameID name text id
    #  @var timeID time text id
    #  @var dateID date text id
    #  @var happyID preference icon happy
    #  @var okID preference icon ok
    #  @var unhappyID preference unhappy icon
    #  @var sphereOneID one sphere id
    #  @var sphereTwoID second sphere id
    #  @var sphereThreeID third sphere id
    #  @var sphereFourID fourth sphere id
    #  @var running running state

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

    ## __init__
    #
    #  constructor for the UI configuration window
    #  @param width window width
    #  @param height window height
    def __init__(self, width, height, conf, dbc):
        self.state = 0
        self.width = width
        self.height = height
        self.configuration = conf
        self.database = dbc
        self.root = Tk()
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.attributes('-fullscreen', True)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.background = Image.open("images/" + conf.image).resize((self.width, self.height),Image.ANTIALIAS)
        self.transparent = Image.open("images/transparency/background-20P.png").resize((self.width, self.height),Image.ANTIALIAS)
        self.background_image = None
        self.tmptrans = None
        self.setStatus(int(conf.bar))

    ## setStatus
    #
    #  change status display style
    #  Sphere display: 0, blur over background: 1,
    #  simpel load bar: 2, combination between 1 and 2: 3
    def setStatus(self, statusStyle):
        print(statusStyle)
        if statusStyle == 0:
            print("Using Spheres")
            self.statusBar = SBSpheres.SBSpheres(400, 50, 6, self.width, self.height, self.canvas)
        elif statusStyle == 1:
            print("Using SBCrossfade")
            self.statusBar = SBCrossfade.SBCrossfade(self.background, self.width, self.height, self.canvas)
        elif statusStyle == 2:
            print("Using bar")
            self.statusBar = SBBar.SBBar(self.width, self.height, 40, self.canvas)
        elif statusStyle == 3:
            print("Using Barfade")
            self.statusBar = SBBarfade.SBBarfade(self.background, self.width, self.height, 40, self.canvas)
        else:
            print("Using Default")
            self.statusBar = SBSpheres.SBSpheres(400, 30, 10, self.width, self.height, self.canvas)

    ## setDateTime
    #
    #  change date time on the display
    #  @param date dateID on screen
    #  @param time timeID on screen
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
        self.canvas.itemconfig(date, text=("" + hour + ":" + minutes))

    ## drawGoal
    #
    #  set goal with black transparent background
    def drawGoal(self, offset):
        self.targetID = self.canvas.create_text(int(abs(self.width / 2)), offset + 20, justify=CENTER, tag="goal", text=self.configuration.goal, width=(self.width-40), fill="white", font=("Helvetica", 30), anchor=CENTER)
        box = self.canvas.bbox(self.targetID)
        bck40 = self.transparent.resize((box[2], box[3]),Image.ANTIALIAS)
        bck40_img = ImageTk.PhotoImage(bck40)
        self.tmptrans = bck40_img
        bck = self.canvas.create_image(int(abs(self.width / 2)),offset + 20, image=bck40_img, anchor=CENTER, tag="goal_box")
        self.canvas.lower("goal_box")
        self.canvas.pack()

    ## Display
    #
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
        try:
            state = self.database.poll()
            self.statusBar.update(state)
        except:
            print("Failed to load data")
            self.statusBar.update(50.0)
        self.setDateTime(self.timeID, self.dateID)

        # Set the background image
        background_s = self.canvas.create_image(0,0, image=self.background_image, anchor=NW)

        # Lower the background image to the back
        self.canvas.lower(background_s)

        #self.displayStateBalls(340, 5, 50, 10)
        self.canvas.pack()
        self.state += 0.1

        # Updater
        if self.running:
            self.root.after(5000, self.display)
        else:
            self.root.quit()

    ## stop
    #
    #  stop the display mainloop
    def stop(self):
        print("stopping main window")
        self.running = False
        self.root.quit()

    ## Start
    #
    # Starts display
    def start(self):
        self.display()
        self.root.mainloop()
