from tkinter import *

root = Tk()

w = root.winfo_screenwidth()  # Get the width of window

h = root.winfo_screenheight()  # Get the height of window

root.geometry("%dx%d+0+0" % (w, h)) # Set app size respective to window size

root.title("Full Screen Window") # Title of screen

root.mainloop()
