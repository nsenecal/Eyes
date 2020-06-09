import tkinter as tk
from tkinter import messagebox
import pynput
import time
import math
import os
from pynput.mouse import Listener

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

selected = False

root = tk.Tk()
root.geometry("120x50")
root.configure(background = "yellow")
root.wm_attributes("-transparentcolor", "yellow")
root.wm_attributes("-topmost", 1)
root.overrideredirect(1)

photo = tk.PhotoImage(file = resource_path("eye.png"))
dot = tk.PhotoImage(file = resource_path("pupil.png"))

eye1 = tk.Label(image = photo, bg = "yellow")
eye2 = tk.Label(image = photo, bg = "yellow")
pupil1 = tk.Label(image = dot, bg = "white")
pupil2 = tk.Label(image = dot, bg = "white")
eye1.place(x=0, y=-2)
eye2.place(x=65, y=-2)
pupil1.place(x=20, y=20)
pupil2.place(x=85, y=20)

def quit(event):
    answer = messagebox.askyesno("Question","Quit the Program?")
    if answer == True:
        import sys
        sys.exit()

def callback(event):
    global selected
    if selected == False:
        selected = True
    else:
        selected = False

def on_move(x, g):
    midX = root.winfo_rootx() + 60
    midY = root.winfo_screenheight() - (root.winfo_rooty() + 10)

    if selected == True:
        root.geometry(("%dx%d%+d%+d" % (120,50,x-30,g-25)))

    y = root.winfo_screenheight() - g

    a = (10*(x-midX+35))/(math.sqrt(((x-midX+35)**2)+(y-midY)**2))
    b = (10*(y-midY))/(math.sqrt(((x-midX+35)**2)+(y-midY)**2))
    pupil1.place(x=20+a, y=20-b)

    c = (10*(x-midX-35))/(math.sqrt(((x-midX-35)**2)+(y-midY)**2))
    d = (10*(y-midY))/(math.sqrt(((x-midX-35)**2)+(y-midY)**2))
    pupil2.place(x=85+c, y=20-d)

root.bind("<Button-1>", callback)
root.bind("<Button-3>", quit)

def on_scroll(x, y, dx, dy):
    pass

oink = Listener(on_move=on_move,on_scroll=on_scroll)
oink.start()

root.mainloop()

oink.stop()
oink.join()
