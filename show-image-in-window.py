from tkinter import *
from PIL import ImageTk, Image #use lib for image if not install using pip install Pillow

root = Tk()
root.iconbitmap('favico.ico')

w, h = root.winfo_screenwidth(), root.winfo_screenheight() # Get the height and width of window
root.geometry("%dx%d+0+0" % (w, h)) # Set app size respective to window size

root.resizable(0,0) # Resize window Disable

root.title("Saree Shop Management")

my_img = ImageTk.PhotoImage(Image.open("img1.jfif")) #place image in same directory
label_img = Label(root,image=my_img)
label_img.pack();

exit_button = Button(root, text="Exit Program", command= root.quit)
exit_button.pack()
root.mainloop()
