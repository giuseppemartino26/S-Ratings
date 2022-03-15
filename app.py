from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Soccer Ratings')

# Read the Image
image = Image.open("soccer.png")
# Resize the image using resize() method
resize_image = image.resize((350, 350))
img = ImageTk.PhotoImage(resize_image)
# Display the image
my_label = Label(image=img)
my_label.grid(row=1, column=1)

myButton = Button(root, text="Click me!",padx=25, pady=25, fg="blue",bg="#ffffff")
myButton.grid(row=2, column=2)



root.mainloop()