from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image

class Rating:

    def __init__(self, root, frame):

        self.root = root
        self.frame = frame

        image = Image.open("back2.png")
        # Resize the image using resize() method
        resize_image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(resize_image)

        myFont2 = font.Font(family='Calibri', size=12)

        Button(self.frame,image=self.img,borderwidth=0,anchor= W,command=self.back).grid(row=0,column=0)

        Label(self.frame,text="\n").grid(row=1,column=0)
        Label(self.frame,text="Is the player a goalkeeper?",font=myFont2).grid(row=2,column=1)
        global var
        var = IntVar()
        Radiobutton(self.frame,text="Yes",variable=var, value=1,font=myFont2).grid(row=2,column=2)
        Radiobutton(self.frame, text="No", variable=var, value=0,font=myFont2).grid(row=2, column=3)

    def back(self):
        self.frame.grid_forget()