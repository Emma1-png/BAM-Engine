import tkinter as tk
from PIL import Image, ImageTk as pi
import math as ma
import json as jsn

# Engine imports
import audioEngine as ae         # Emits audio when needed
import flatRenderer as fr        # Renders the shaoe of the .png given
import lightEngine as le         # Renders light
import textureRenderer as tr     # Renders the textures on top of flatRenderer

class FrontEnd:
    def __init__(self, windowSizeX, windowSizeY):
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY

        # Defined afterwards
        self.projectName = None
        self.projectDescription = None
        self.savePath = None
    
    def InitialiseWindow(self):
        wn = tk.Tk()
        wn.geometry(f"{self.windowSizeX}x{self.windowSizeY}")

        with open("ENGINEDATA.tmp", "r") as f:
            fileContents = f.read()
            print(fileContents)
            self.projectName = fileContents
        
        wn.title(f"BAM! Engine - {self.projectName}")
        
        wn.resizable(0, 0)
        
        self.wn = wn
        
    def WindowDisplay(self):
        '''
        This is for all of the buttons and various items within the frontend of the engine
        Along with all of the borders for the sections in the app (see DevlogAndNotes.txt)
        '''

        self.c = tk.Canvas(self.wn, width=self.windowSizeX, height=self.windowSizeY)
        self.c.pack(fill="both", expand=True)
        
        x1 = 200
        x2 = 650

        y1 = 30
        y2 = 350
        y3 = 375
        y4 = 55

        widthMain = 4
        widthSeperator = 2
        widthHighlight = 3

        # General Lines
        BarrierLine = c.create_line(0, y1, self.windowSizeX, y1, width=widthMain)

        HierachyLine = c.create_line(x1, y1, x1, self.windowSizeY, width=widthSeperator)

        OptionsLine = c.create_line(x2, y1, x2, y2, width=widthSeperator)
        OptionsSeperatorLine = c.create_line(x2, y4, self.windowSizeX, y4, width=widthHighlight)

        ProjectLine = c.create_line(x1, y2, self.windowSizeX, y2, width=widthSeperator)
        ProjectSeperatorLine = c.create_line(x1, y3, self.windowSizeX, y3, width=widthHighlight)

        # General (No Commands Given) Buttons
        RunButton = tk.Button(c, text="▶")
        RunButton.place(x=width/2, y=0)

        AssetsButton = tk.Button(c, text="Assets")
        AssetsButton.place(x=205, y=354)

        LogsButton = tk.Button(c, text="Logs")
        LogsButton.place(x=255, y=354)

        HelpButton = tk.Button(c, text="Help")
        HelpButton.place(x=300, y=354)
        
        self.wn.mainloop()

class BackEnd:
    def __init__(self):
        pass
    
    def Save(self):
        #with open("projects.json", "a") as f:
            #self.saveLocation = 
        #with open("
        pass
        
    def ReadJSON(self, option):
        with open("projects.json", "r") as f:
            data = jsn.load(f)
            ''' Not needed yet.
            if option == "ProjectName":
                for project in data["projects"]:
                    print(project["ProjectName"], "->", project["SavePath"])
                    '''

if __name__ == "__main__":
    fe = FrontEnd(900, 500)
    be = BackEnd()
    fe.InitialiseWindow()
    fe.WindowDisplay()
