############
# LAUNCHER #
############

import tkinter as tk
from PIL import Image, ImageTk
import json as jsn
from datetime import datetime as dt
import loader as ld

height = 320

wn = tk.Tk()
wn.geometry("500x320")
wn.title("BAM! Engine Launcher")

# --- Canvas as the main surface ---
c = tk.Canvas(wn, width=500, height=height, highlightthickness=0)
c.pack(fill="both", expand=True)

##################
# FRONTEND LOOKS #
##################

# --- Logo ---
img = Image.open("FullLogo.png")
img = img.resize((90, 45))
bamLogoFull = ImageTk.PhotoImage(img)

logo = tk.Label(c, image=bamLogoFull)
c.create_window(0, 0, anchor="nw", window=logo)

# --- Buttons --- 
loadProjectButton = tk.Button(c, text="- | Load Other", relief="raised", bd=4)
c.create_window(300, 10, anchor="nw", window=loadProjectButton)


newProjectButton = tk.Button(c, text="+ | New Project", relief="raised", bd=4)
c.create_window(490, 10, anchor="ne", window=newProjectButton)

buttonXPosition = 485

# - Load Project Buttons -
loadRecentProjectButton1 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(buttonXPosition, 85, anchor="ne", window=loadRecentProjectButton1)

loadRecentProjectButton2 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(buttonXPosition, 145, anchor="ne", window=loadRecentProjectButton2)

loadRecentProjectButton3 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(buttonXPosition, 205, anchor="ne", window=loadRecentProjectButton3)

loadRecentProjectButton4 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(buttonXPosition, 265, anchor="ne", window=loadRecentProjectButton4)

# --- Line(s) ---
c.create_line(0, 63, 500, 63, fill="black", width=7) # Top (thick) line

# - Other Horizontal Lines
hLine1Y = 120
c.create_line(0, hLine1Y, 500, hLine1Y, fill="black", width=2)

hLine2Y = 180
c.create_line(0, hLine2Y, 500, hLine2Y, fill="black", width=2)

hLine3Y = 240
c.create_line(0, hLine3Y, 500, hLine3Y, fill="black", width=2)

hLine4Y = 300
c.create_line(0, hLine4Y, 500, hLine4Y, fill="black", width=2)

# - Vertical Lines -
vLine1X = 100
c.create_line(vLine1X, 63, vLine1X, 320, fill="black", width=1)

vLine2X = 390
c.create_line(vLine2X, 63, vLine2X, 320, fill="black", width=1)

# ============================================================================================================ #
#################
# BACKEND WORKS #
#################

with open("projects.json", "r") as file:
    data = jsn.load(file)

def readProjectsJSONFile():
    global data
    global loadRecentProjectButton1, loadRecentProjectButton2, loadRecentProjectButton3, loadRecentProjectButton4
    
    projects = data["projects"]
    
    # Sadly, given by AI, but I have no other clue about how to do this
    projects.sort(
        key=lambda p: dt.strptime(p["LastEdited"], "%d/%m/%Y"),
        reverse=True
    )
    # AI written section ends here
    
    startY = 82
    stepY = 60
    
    slotsFilled = 0
    
    # TO NOTE: The projects.json properties "RenderType" and "SavePath" are for the engine backend to decipher, it is not for reading in the launcher
    for project in projects:
        # The prints are for debugging only. Change the IF STATEMENT from False to True (line below) when needed.
        if False:
            print(f"Project Name: {project['ProjectName']}")
            print(f"Project Descripton: {project['ProjectDescription']}")
            print(f"Last Modified: {project['LastEdited']}")
            print("--------------------------------------------------------------------")
        projectName = project['ProjectName']
        projectDescription = project['ProjectDescription']
        projectLastModified = project['LastEdited']
        
        # Set the titles
        projectTitle = tk.Label(c, text=projectName)
        projectTitle.place(x=5, y=startY)
        
        # Set the descriptions
        projectDescr = tk.Label(c, text=projectDescription)
        projectDescr.place(x=105, y=startY-15)
        
        # Set the dates
        # Extra work required here
        currentDate = dt.now()
        lastEditedDate = dt.strptime(projectLastModified, "%d/%m/%Y")
        
        daysAgo = (currentDate - lastEditedDate).days
        
        projectDate = tk.Label(c, text=f"Edited {daysAgo} days ago")
        projectDate.place(x=395, y=startY-15)
        
        slotsFilled += 1
        startY += stepY
    
    if slotsFilled >= 1:
        loadRecentProjectButton1.config(state=tk.NORMAL)
    if slotsFilled >= 2:
        loadRecentProjectButton2.config(state=tk.NORMAL)
    if slotsFilled >= 3:
        loadRecentProjectButton3.config(state=tk.NORMAL)
    if slotsFilled == 4:
        loadRecentProjectButton4.config(state=tk.NORMAL)

readProjectsJSONFile()

# Enable loader
def launchProjectCreator():
    launcher = ld.frontEnd(500, 600)
    launcher.openWindow() # Open the new window
newProjectButton.config(command=launchProjectCreator)

# --- Mainloop ---
wn.mainloop()
