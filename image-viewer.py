from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('favico.ico')
w, h = root.winfo_screenwidth(), root.winfo_screenheight() # Get the height and width of window
root.geometry("%dx%d+0+0" % (w, h)) # Set app size respective to window size
root.resizable(0,0) # Resize window Disable
root.title("Saree Shop Management")

my_img1 = ImageTk.PhotoImage(Image.open("saree1.jpg").resize((200,200)))
my_img2 = ImageTk.PhotoImage(Image.open("saree2.jpg").resize((200,200)))
my_img3 = ImageTk.PhotoImage(Image.open("saree3.jpg").resize((200,200)))
my_img4 = ImageTk.PhotoImage(Image.open("saree4.jpg").resize((200,200)))
my_img5 = ImageTk.PhotoImage(Image.open("saree5.jpg").resize((200,200)))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

def nextImage(number):
    global my_label
    global next_button
    global pre_button
    my_label.grid_forget()
    my_label = Label(root, image=image_list[number+1], height=200, width=200)
    next_button = Button(root,text="Next", command=lambda : nextImage(number+1))
    next_button.grid(row=1, column=2)
    if number == 5:
        next_button = Button(root,text="Next",state=DISABLED)
    pre_button = Button(root,text="Pre", command=lambda : preImage(number-1))
    pre_button.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)

def preImage(number):
    global my_label
    global next_button
    global pre_button
    my_label.grid_forget()
    my_label = Label(root, image=image_list[number - 1], height=200, width=200)
    next_button = Button(root, text="Next", command=lambda: nextImage(number + 1))
    next_button.grid(row=1, column=2)
    pre_button = Button(root, text="Pre", command=lambda: preImage(number - 1))
    pre_button.grid(row=1, column=0)
    if number == 1:
        pre_button = Button(root,text="Pre",state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)

my_label = Label(root,image=my_img1,height=200,width=200)
my_label.grid(row=0,column=0,columnspan=3)

next_button = Button(root,text="Next",command=lambda: nextImage(2))
next_button.grid(row=1,column=2)

pre_button = Button(root,text="Pre",command=lambda: preImage(1))
pre_button.grid(row=1,column=0)

exit_button = Button(root, text="Exit Program", command= root.quit)
exit_button.grid(row=1,column=1)
root.mainloop()
