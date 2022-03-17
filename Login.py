from tkinter import *
from PIL import ImageTk,Image

from Panel import Panel


class Login:
    def __init__(self):

        self.root = Tk()
        self.root.title('Soccer Ratings')

        image = Image.open("soccer.png")
        # Resize the image using resize() method
        resize_image = image.resize((350, 100))
        self.img = ImageTk.PhotoImage(resize_image)
        self.label_img = Label(self.root, image=self.img)
        self.label_img.grid(row=0, column=0, columnspan=3)

        self.frame = LabelFrame(self.root, pady=100, padx=100)
        self.frame.grid(row=2, column=1)

        self.panel = Panel(self.root, self.frame)



    def start(self):
        self.root.mainloop()