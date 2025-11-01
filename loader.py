import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import json as jsn

class frontEnd:
    def __init__(self, windowSizeX, windowSizeY):
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        
    def openWindow(self):
        wn = tk.Tk()
        wn.geometry(f"{self.windowSizeX}x{self.windowSizeY}")
        wn.title("BAM! Engine Project Creator")
        
        
        # Initialise canvas features within the window
        c = tk.Canvas(wn, width=self.windowSizeX, height=self.windowSizeY)
        c.pack(fill="both", expand=True)
        
        # Engine Title/Logo
        img = Image.open("FullLogo.png")
        img = img.resize((110, 65))
        bamLogoFull = ImageTk.PhotoImage(img)
        logo = tk.Label(c, image=bamLogoFull)
        c.create_window(0, 0, anchor="nw", window=logo)
        
        # Window Title
        windowTitle = tk.Label(c, text="NEW PROJECT", font=("Helvetica", 16, "bold"))
        windowTitle.place(x=320, y=28)
        
        # Bar
        barY = 75
        c.create_line(0, barY, 500, barY, fill="black", width=7)
        
        # Project Naming Area
        projectNameLabel = tk.Label(c, text="PROJECT NAME", font=("Helvetica", 14, "bold"))
        projectNameLabel.place(x=0, y=100)
        #     #
        projectNameTextBox = tk.Entry(c, width=30, font=("Helvetica", 9, "italic"))
        projectNameTextBox.place(x=10, y=130)
        
        # Project Description Area
        projectDescriptionLabel = tk.Label(c, text="PROJECT DESCRIPTION", font=("Helvetica", 14, "bold"))
        projectDescriptionLabel.place(x=0, y=160)
        #     #
        projectDescriptionTextBox = tk.Text(c, height=5, width=68, font=("Helvetica", 9))
        projectDescriptionTextBox.place(x=10, y=190)
        
        # Project Render Type
        # Radio Buttons
        projectRendererType = tk.Label(c, text="RENDER TYPE", font=("Helvetica", 14, "bold"))
        projectRendererType.place(x=10, y=290)
        # AI  #
        choice = tk.StringVar(value="2D") # Default
        
        buttonSize = 15
        choice1 = tk.Radiobutton(c, text="2D", variable=choice, value="2D", font=("Helvetica", buttonSize, "bold"))
        choice2 = tk.Radiobutton(c, text="3D", variable=choice, value="3D", font=("Helvetica", buttonSize, "bold"))
        choice1.place(x=20, y=310)
        choice2.place(x=100, y=310)
        
        # AI ENDS #
        
        # Save Location Area
        saveLocationLabel = tk.Label(c, text="SAVE TO:", font=("Helvetica", 14, "bold"))
        saveLocationLabel.place(x=350, y=100)
        
        saveLocationButton = tk.Button(c, text="\U0001F4C2", font=("Helvetica", 16, "bold")) # I don't think that'll do anything
        saveLocationButton.place(x=375, y=125)
        
        # Submit Button
        submitLabel = tk.Label(c, text="CREATE?", font=("Helvetica", 13, "bold"))
        submitLabel.place(x=200, y=290)
        
        submitButton = tk.Button(c, text="Create", font=("Helvetica", 10))
        submitButton.place(x=207, y=310)
        
        # Tie to backend functions
        be = backEnd(projectNameTextBox, projectDescriptionTextBox, choice)
        submitButton.config(command=be.compileInformation)
        saveLocationButton.config(command=be.chooseSaveLocation)
        
        wn.mainloop()
        
        return projectNameTextBox, projectDescriptionTextBox, choice, submitButton # Not sure how to grab "saveLocationButton" data, probably another backend function required

class backEnd:
    def __init__(self, nameBox, descriptionBox, choiceVar):
        self.nameBox = nameBox
        self.descriptionBox = descriptionBox
        self.choiceVar = choiceVar
        self.saveLocation = None # Selected later in chooseSaveLocation
    
    def compileInformation(self):
        projectName = self.nameBox.get()
        projectDescription = self.descriptionBox.get("1.0", tk.END).strip()
        renderer = self.choiceVar.get()
        
        # DEBUG - change to TRUE
        if True:
            print(f"Project Name: {projectName} \nProject Description: {projectDescription} \nProject Renderer: {renderer}\nSave Location: {self.saveLocation}")
            
    def chooseSaveLocation(self):
        locationChosen = filedialog.askdirectory(title="Select Save Location")
        if locationChosen:
            print(f"Save Location Chosen: {locationChosen}")
            self.saveLocation = locationChosen

if __name__ == "__main__":
    print("Frontend Loading...")
    fe = frontEnd(500, 345)
    fe.openWindow()