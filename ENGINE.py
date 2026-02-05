"""
(
    BAM! ENGINE - Version 1
)
(
    CODE HEADERS (update every session):
    SET UP THE WINDOW: ln 27
    INITIALISE CANVAS: ln 33
    SET UP SCREEN SECTIONS: ln 40
    TOOLBAR CONFIG: ln 55
             --
    3D MODELLING FUNCTIONS: ln 162
    2D DESIGN FUNCTIONS: ln 168
    PROGRAMMING FUNCTIONS: ln 174
    TERMINAL FUNCTIONS: ln 184
    HIERACHY FUNCTIONS: ln 195
    ASSET FUNCTIONS: ln 206
    RENDERING FUNCTIONS: ln 207
    PROPERTIES FUNCTIONS: ln 229
             --
    BACK-END FUNCTIONS: ln 240
)
"""

import tkinter as tk

# SET UP THE WINDOW
###################
wn = tk.Tk()
wn.title("Bam! Engine - Attempt 1 (tkinter & GUI)")
wn.resizable(False, False)

# Initialise Canvas
###################
SCREENWIDTH = 950
SCREENHEIGHT = 650
c = tk.Canvas(wn, width=SCREENWIDTH, height=SCREENHEIGHT, bg="#F0F0F0")
c.pack()

# Set Up Screen Sections
########################
# Maths
x1 = SCREENWIDTH / 4
y1 = SCREENHEIGHT - x1 + 25
x2 = SCREENWIDTH / 4 + SCREENWIDTH / 2
y2 = SCREENHEIGHT / 20

# Create The Lines
toolbarLine = c.create_line(0, y2, SCREENWIDTH, y2, width=2)
propertiesLine = c.create_line(x1, y2, x1, y1, width=3)
assetsLine = c.create_line(0, y1, SCREENWIDTH, y1, width=3)
hierachyLine = c.create_line(x2, y2, x2, y1, width=3)
terminalLine = c.create_line(x2, y1, x2, SCREENHEIGHT, width=3)

# TOOLBAR CONFIG
################
# Button Booleans
fileBool = False
editBool = False
runBool = False
helpBool = False

# Windows
fileWindow = c.create_rectangle(0, 35, 145, 140, fill="#E7FF78", width=0, state=tk.HIDDEN)
editWindow = c.create_rectangle(50, 35, 195, 140, fill="#78A1FF", width=0, state=tk.HIDDEN)
runWindow = c.create_rectangle(101, 35, 246, 140, fill="#FF7878", width=0, state=tk.HIDDEN)
helpWindow = c.create_rectangle(152, 35, 297, 140, fill="#FF78E6", width=0, state=tk.HIDDEN)

# Give Functions to Each Button
class toolBarFunctions:
    def closeOtherWindows(closeFile, closeEdit, closeRun, closeHelp):
        # FILE
        global fileBool
        global fileWindow
        # EDIT
        global editBool
        global editWindow
        # RUN
        global runBool
        global runWindow
        # HELP
        global helpBool
        global helpWindow

        bools = False
        if closeFile:
            print("CloseFile")

            editBool = bools
            runBool = bools
            helpBool = bools

            c.itemconfig(editWindow, state=tk.HIDDEN)
            c.itemconfig(runWindow, state=tk.HIDDEN)
            c.itemconfig(helpWindow, state=tk.HIDDEN)
        if closeEdit:
            print("CloseEdit")
            
            fileBool = bools
            runBool = bools
            helpBool = bools

            c.itemconfig(fileWindow, state=tk.HIDDEN)
            c.itemconfig(runWindow, state=tk.HIDDEN)
            c.itemconfig(helpWindow, state=tk.HIDDEN)
        if closeRun:
            print("CloseRun")
            
            fileBool = bools
            editBool = bools
            helpBool = bools

            c.itemconfig(fileWindow, state=tk.HIDDEN)
            c.itemconfig(editWindow, state=tk.HIDDEN)
            c.itemconfig(helpWindow, state=tk.HIDDEN)
        if closeHelp:
            print("CloseHelp")
            
            fileBool = bools
            editBool = bools
            runBool = bools

            c.itemconfig(fileWindow, state=tk.HIDDEN)
            c.itemconfig(editWindow, state=tk.HIDDEN)
            c.itemconfig(runWindow, state=tk.HIDDEN)
            

    def fileButtonFunction():
        """Opens/Closes the File Function Window"""
        global fileBool
        global fileWindow
        
        if not fileBool: # Opens the window
            print("False: FileBool")
            c.itemconfig(fileWindow, state=tk.NORMAL)
        else: # Closes the window
            print("True: FileBool")
            c.itemconfig(fileWindow, state=tk.HIDDEN)
        
        fileBool = not fileBool
        toolBarFunctions.closeOtherWindows(True, False, False, False)
        
    def editButtonFunction():
        """Opens/Closes the Edit Function Window"""
        global editBool
        global editWindow
        
        if not editBool: # Opens the window
            print("False: EditBool")
            c.itemconfig(editWindow, state=tk.NORMAL)
        else: # Closes the window
            print("True: EditBool")
            c.itemconfig(editWindow, state=tk.HIDDEN)

        editBool = not editBool
        toolBarFunctions.closeOtherWindows(False, True, False, False)
        
    def runButtonFunction():
        """Opens/Closes the Run Function Window"""
        global runBool
        global runWindow
        
        if not runBool: # Opens the window
            print("False: RunBool")
            c.itemconfig(runWindow, state=tk.NORMAL)
        else: # Closes the window
            print("True: RunBool")
            c.itemconfig(runWindow, state=tk.HIDDEN)

        runBool = not runBool
        toolBarFunctions.closeOtherWindows(False, False, True, False)
        
    def helpButtonFunction():
        """Opens/Closes the Help Function Window"""
        global helpBool
        global helpWindow
        
        if not helpBool: # Opens the window
            print("False: HelpWindow")
            c.itemconfig(helpWindow, state=tk.NORMAL)
        else: # Closes the window
            print("True: HelpWindow")
            c.itemconfig(helpWindow, state=tk.HIDDEN)

        helpBool = not helpBool
        toolBarFunctions.closeOtherWindows(False, False, False, True)

# Initialise Buttons
fileButton = tk.Button(wn, text="File", bd=0, fg="#E7FF78", bg="#FEFEFE", command=toolBarFunctions.fileButtonFunction)
fileButton.place(x=0, y=0)

editButton = tk.Button(wn, text="Edit", bd=0, fg="#78A1FF", bg="#FEFEFE", command=toolBarFunctions.editButtonFunction)
editButton.place(x=50, y=0)

runButton = tk.Button(wn, text="Run", bd=0, fg="#FF7878", bg="#FEFEFE", command=toolBarFunctions.runButtonFunction)
runButton.place(x=101, y=0)

helpButton = tk.Button(wn, text="Help", bd=0, fg="#FF78E6", bg="#FEFEFE", command=toolBarFunctions.helpButtonFunction)
helpButton.place(x=152, y=0)

# 3D MODELLING FUNCTIONS
#######################
class modellingWindow:
    def __init__(self):
        pass

# 2D DESIGN FUNCTIONS
#####################
class designWindow:
    def __init__(self):
        pass

# PROGRAMMING FUNCTIONS
#######################
# Expect this class to be VERY LONG
class programmingWindow:
    class compiler:
        def __init__(self):
            pass
    
    def __init__(self):
        pass

# TERMINAL FUNCTIONS
####################
class terminalWindow:
    def __init__(self, twx1, twy1, twx2, twy2):
        # Terminal Window (x)
        self.twx1 = twx1
        self.twx2 = twx2
        # Terminal Window (y)
        self.twy1 = twy1
        self.twy2 = twy2

        # Lines in the terminal
        self.lines = 1
        self.lineSpacing = 15
    
    def setupBackground(self, backgroundHex: str):
        self.background = c.create_rectangle(self.twx1, self.twy1, self.twx2, self.twy2, fill=backgroundHex, width=3)
    
    def addLine(self, textTitle: str, text: str, textTitleColour: str, textColour: str):
        c.create_text(self.twx1+5, self.twy1+(self.lines*self.lineSpacing), text=textTitle, fill=textTitleColour, anchor=tk.W)

        # FIX HERE
        ##########
        
        gapping = 0
        for i in range(len(textTitle)):
            gapping += 5
        print(len(textTitle))
        
        c.create_text(self.twx1+5+gapping, self.twy1+(self.lines*self.lineSpacing), text=text, fill=textColour, anchor=tk.W) # FIX HERE!!!!
        self.lines += 1

# HIERACHY FUNCTIONS
####################
class hierachyWindow:
    def __init__(self, hwx1, hwy1, hwx2, hwy2):
        # Hierachy Window (x)
        self.hwx1 = hwx1
        self.hwx2 = hwx2
        # Hierachy Window (y)
        self.hwy1 = hwy1
        self.hwy2 = hwy2

# ASSET FUNCTIONS
#################
class assetWindow:
    def __init__(self, awx1, awy1, awx2, awy2):
        # Assets Window (x)
        self.awx1 = awx1
        self.awx2 = awx2
        # Assets Window (y)
        self.awy1 = awy1
        self.awy2 = awy2

# RENDERING FUNCTIONS
#####################
# Expect this class to be VERY LONG
class renderingWindow:
    def __init__(self, rwx1, rwy1, rwx2, rwy2):
        # Rendering Window (x)
        self.rwx1 = rwx1
        self.rwx2 = rwx2
        # Rendering Window (y)
        self.rwy1 = rwy1
        self.rwy2 = rwy2

# PROPERTIES FUNCTIONS
######################
class propertiesWindow:
    def __init__(self, pwx1, pwy1, pwx2, pwy2):
        # Programming Window (x)
        self.pwx1 = pwx1
        self.pwx2 = pwx2
        # Programming Window (y)
        self.pwy1 = pwy1
        self.pwy2 = pwy2

# BACK-END FUNCTIONS
####################
"""
This subsection entails the following:
1- Background Math
2- Light Rendering: Called by "RENDERING FUNCTIONS"
3- Sound Rendering
4- Opening system windows, eg file explorer
5- Reading the project folder
6- Saving to the project folder
and much more
"""
class backend:
    class BackgroundMath:
        def __init__(self):
            pass
    
    class System:
        """
        - Look at 4,5,6 on subsection description
        """
        def __init__(self):
            pass

tw = terminalWindow(x2, y1, SCREENWIDTH, SCREENHEIGHT)
hw = hierachyWindow(x2, y2, SCREENWIDTH, y1)
aw = assetWindow(0, y1, x2, SCREENHEIGHT)
rw = renderingWindow(x1, y2, x2, y1)
pw = propertiesWindow(0, y2, x1, y1)

# TW
tw.setupBackground("#000000")
tw.addLine("PRINT: ", "TESTING 1", "#1F1FFF", "#00FF00")
tw.addLine("WARNING: ", "TESTING 2", "#FFA500", "#00FF00")
tw.addLine("ERROR: ", "TESTING 3", "#FF0000", "#00FF00")

################################
# ENSURE THE WINDOW STAYS OPEN #
################################
wn.mainloop()
