from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('favico.ico')
w, h = root.winfo_screenwidth(), root.winfo_screenheight() # Get the height and width of window
root.geometry("%dx%d+0+0" % (w, h)) # Set app size respective to window size
root.resizable(0,0) # Resize window Disable
root.title("Tkinter Programs")

labelFrame = LabelFrame(root,text="This is frame example",padx=10,pady=10)
labelFrame.pack()

button = Button(labelFrame,text="Click Here")
button.pack()

root.mainloop()
