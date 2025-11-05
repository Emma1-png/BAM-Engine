import tkinter as tk
import PIL as pi
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
            
            if option == "ProjectName":
                for project in data["projects"]:
                    print(project["ProjectName"], "->", project["SavePath"])

if __name__ == "__main__":
    fe = FrontEnd(900, 500)
    be = BackEnd()
    fe.InitialiseWindow()
    fe.WindowDisplay()
