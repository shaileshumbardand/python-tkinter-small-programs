from tkinter import *

root = Tk()
root.iconbitmap('favico.ico')

w, h = root.winfo_screenwidth(), root.winfo_screenheight() # Get the height and width of window

root.geometry("%dx%d+0+0" % (w, h)) # Set app size respective to window size

root.resizable(0,0) # Resize window Disable

root.title("Saree Shop Management")

exit_button = Button(root, text="Exit Program", command= root.quit)
exit_button.pack()

root.mainloop()
