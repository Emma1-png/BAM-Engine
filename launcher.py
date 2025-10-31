############
# LAUNCHER #
############

import tkinter as tk
from PIL import Image, ImageTk

height = 320

wn = tk.Tk()
wn.geometry("500x320")
wn.title("BAM! Engine Launcher")

# --- Canvas as the main surface ---
c = tk.Canvas(wn, width=500, height=height, highlightthickness=0)
c.pack(fill="both", expand=True)

# --- Logo ---
img = Image.open("FullLogo.png")
img = img.resize((90, 45))
bamLogoFull = ImageTk.PhotoImage(img)

logo = tk.Label(c, image=bamLogoFull)
c.create_window(0, 0, anchor="nw", window=logo)

# --- Buttons --- 
loadProjectButton = tk.Button(c, text="- | Load Other")
c.create_window(300, 10, anchor="nw", window=loadProjectButton)

newProjectButton = tk.Button(c, text="+ | New Project")
c.create_window(490, 10, anchor="ne", window=newProjectButton)

# - Load Project Buttons -
loadRecentProjectButton1 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(490, 90, anchor="ne", window=loadRecentProjectButton1)

loadRecentProjectButton2 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(490, 150, anchor="ne", window=loadRecentProjectButton2)

loadRecentProjectButton3 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(490, 210, anchor="ne", window=loadRecentProjectButton3)

loadRecentProjectButton4 = tk.Button(c, text="Load Project", state=tk.DISABLED)
c.create_window(490, 270, anchor="ne", window=loadRecentProjectButton4)
# --- Line(s) ---
c.create_line(0, 63, 500, 63, fill="black", width=7)

# WATCH THIS SPACE

# --- Mainloop ---
wn.mainloop()
