from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/",title = "Open file you wish to utilise")
root.destroy()
dataPath_string = root.filename