import tkinter as tk
import pynput
import time
import math
root = tk.Tk()
root.geometry("120x50")
root.wm_attributes("-topmost", 1)
root.overrideredirect(1)
canvas = tk.Canvas(root, width = 120, height = 50)

photo = tk.PhotoImage(file = "eye.png")
dot = tk.PhotoImage(file = "pupil.png")

eye1 = tk.Label(image = photo)
eye2 = tk.Label(image = photo)
pupil1 = tk.Label(image = dot)
pupil2 = tk.Label(image = dot)
eye1.place(x=0, y=-2)
eye2.place(x=65, y=-2)

while True:
    root.update()
    midX = root.winfo_rootx() + 60
    midY = root.winfo_screenheight() - (root.winfo_rooty() + 10)

    try:
        x, g = pynput.mouse.Controller().position
    except TypeError:
        pass
    else:
        y = root.winfo_screenheight() - g

        a = (10*(x-midX+35))/(math.sqrt(((x-midX+35)**2)+(y-midY)**2))
        b = (10*(y-midY))/(math.sqrt(((x-midX+35)**2)+(y-midY)**2))
        pupil1.place(x=20+a, y=20-b)

        c = (10*(x-midX-35))/(math.sqrt(((x-midX-35)**2)+(y-midY)**2))
        d = (10*(y-midY))/(math.sqrt(((x-midX-35)**2)+(y-midY)**2))
        pupil2.place(x=85+c, y=20-d)

    time.sleep(0.01)
root.mainloop()
