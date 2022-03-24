from tkinter import *
from PIL import ImageTk, Image

from Panel import Panel
from tkinter import messagebox
import tkinter.font as font
import mysql.connector


from database import Database

db = Database()


class Login:


    def check(self, username, password):
        stmt = "SELECT count(*) FROM users WHERE Username = %s AND Password = %s"
        data = (username, password)
        db.mycursor.execute(stmt, data)
        result = db.mycursor.fetchall()
        if int(result[0][0]) >= 1:
            return True
        else:
            return False

    def check_only_us(self, username):
        stmt = "SELECT count(*) FROM users WHERE Username = %s"
        data = [username]
        db.mycursor.execute(stmt, data)
        result = db.mycursor.fetchall()
        if int(result[0][0]) >= 1:
            return True
        else:
            return False

    def log(self,username, password):
        if self.check(username, password):
            Panel(self.root, self.frame2, str(self.user_entry.get()))
            self.frame2.grid(row=2, column=1)
        else:
            messagebox.showerror("Error", "Credentials not valid, please retry.")


    def register(self,username,password):
        if self.check_only_us(username):
            messagebox.showerror("Error", "Username already used, please choose another one")
        else:
            stmt = "INSERT INTO users (`Username`, `Password`) VALUES (%s,%s);"
            data = (username,password)
            db.mycursor.execute(stmt,data)
            messagebox.showinfo("Success","Successful Registration")



    def __init__(self):

        self.root = Tk()
        self.root.title('Soccer Ratings')

        image = Image.open("soccer.png")
        # Resize the image using resize() method
        resize_image = image.resize((350, 100))
        self.img = ImageTk.PhotoImage(resize_image)
        self.label_img = Label(self.root, image=self.img)
        self.label_img.grid(row=0, column=0, columnspan=3)

        # global frame

        self.frame = LabelFrame(self.root, pady=100, padx=100)
        self.frame.grid(row=2, column=1)

        self.frame2 = LabelFrame(self.root, pady=100, padx=100)

        myFont = font.Font(family='Calibri', size=12)
        user_label = Label(self.frame, text="Username: ", font=myFont)
        pass_label = Label(self.frame, text="Password: ", font=myFont)
        space_label1 = Label(self.frame, text=" ")
        space_label2 = Label(self.frame, text=" ")

        self.user_entry = Entry(self.frame, width=17, font=myFont)
        self.user_entry.grid(row=2, column=2)

        pass_entry = Entry(self.frame, width=17, font=myFont, show='*')
        user_label.grid(row=2, column=1)

        space_label1.grid(row=3, column=1)
        pass_label.grid(row=4, column=1)
        pass_entry.grid(row=4, column=2)
        # login_button = Button(self.frame, text="Login", padx=20, pady=7, bg="#4eb6b0", font=myFont, command=lambda: self.funzione(str(user_entry.get())))
        login_button = Button(self.frame, text="Login", padx=20, pady=7, bg="#4eb6b0", font=myFont,
                              command=lambda: self.log(str(self.user_entry.get()), str(pass_entry.get())))

        space_label2.grid(row=5, column=1)
        login_button.grid(row=6, column=2)

        space_label5 = Label(self.frame, text="\n" + "\n")
        space_label5.grid(row=7, column=1)

        user_label2 = Label(self.frame, text="Username: ", font=myFont)
        pass_label2 = Label(self.frame, text="Password: ", font=myFont)
        space_label3 = Label(self.frame, text=" ")
        space_label4 = Label(self.frame, text=" ")
        user_entry2 = Entry(self.frame, width=17, font=myFont)
        pass_entry2 = Entry(self.frame, width=17, font=myFont, show='*')
        user_label2.grid(row=8, column=1)
        user_entry2.grid(row=8, column=2)
        space_label3.grid(row=9, column=1)
        pass_label2.grid(row=10, column=1)
        pass_entry2.grid(row=10, column=2)
        login_button2 = Button(self.frame, text="Register", padx=20, pady=7, bg="#1d434e", fg="white", font=myFont, command=lambda: self.register(str(user_entry2.get()),str(pass_entry2.get())))
        space_label4.grid(row=11, column=1)
        login_button2.grid(row=12, column=2)

        space_label6 = Label(self.frame, text="                                             ")
        # space_label6.grid(row=1,column=4)

        space_label13 = Label(self.frame, text="\n" + "\n")

    def start(self):
        self.root.mainloop()
