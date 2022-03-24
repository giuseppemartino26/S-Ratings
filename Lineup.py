from database import Database
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

db = Database()
global clicked

class Lineup:

    def back(self):
        #self.frame_mov.grid_forget()
        #self.frame_gk.grid_forget()
        self.frame.grid_forget()


    def compute_list(self, username, role, num):
        final_list = []
        stmt_p = "select p1.Player, avg(p1.rating) as avg_rating from Performance p1 where p1.role = %s and p1.Username = %s and (select count(*) from Performance p2 where p1.Player = p2.Player and p1.Date <= p2.Date) <=2 group by p1.Player"
        data_p = [role, username]
        db.mycursor.execute(stmt_p,data_p)
        result_p = db.mycursor.fetchall()
        sorted_result = sorted(result_p, key=lambda tup: tup[1], reverse=True)

        for i in range(num):
            final_list.append(sorted_result[i][0])

        return final_list





    def display_lineup(self, choice):

        if choice == '4-4-2':
            fw_list = self.compute_list(self.username,'Forewarder', 2)
            print(fw_list)

            Label(self.frame_442, text= fw_list[0],font=self.myFont2).grid(row=6, column=2)
            Label(self.frame_442, text= "        ").grid(row=6,column=3)
            Label(self.frame_442, text=fw_list[1], font=self.myFont2).grid(row=6, column=4)

            Label(self.frame_442, text="\n"+"\n").grid(row=5, column=0)

            mf_list = self.compute_list(self.username, 'Midfielder', 4)
            Label(self.frame_442, text=mf_list[0], font=self.myFont2).grid(row=4, column=0)
            Label(self.frame_442, text="        ").grid(row=4, column=1)
            Label(self.frame_442, text=mf_list[1], font=self.myFont2).grid(row=4, column=2)
            Label(self.frame_442, text="        ").grid(row=4, column=3)
            Label(self.frame_442, text=mf_list[2], font=self.myFont2).grid(row=4, column=4)
            Label(self.frame_442, text="        ").grid(row=4, column=5)
            Label(self.frame_442, text=mf_list[3], font=self.myFont2).grid(row=4, column=6)

            Label(self.frame_442, text="\n" + "\n").grid(row=3, column=0)

            df_list = self.compute_list(self.username, 'Defensor', 4)
            Label(self.frame_442, text=df_list[0], font=self.myFont2).grid(row=2, column=0)
            Label(self.frame_442, text="        ").grid(row=2, column=1)
            Label(self.frame_442, text=df_list[1], font=self.myFont2).grid(row=2, column=2)
            Label(self.frame_442, text="        ").grid(row=2, column=3)
            Label(self.frame_442, text=df_list[2], font=self.myFont2).grid(row=2, column=4)
            Label(self.frame_442, text="        ").grid(row=2, column=5)
            Label(self.frame_442, text=df_list[3], font=self.myFont2).grid(row=2, column=6)

            Label(self.frame_442, text="\n" + "\n").grid(row=1, column=0)

            df_list = self.compute_list(self.username, 'Goalkeeper', 1)
            Label(self.frame_442, text=df_list[0], font=self.myFont2).grid(row=0, column=1, columnspan=5)



            self.frame_442.grid(row=3, column=1)
            self.frame_442.tkraise()








    def __init__(self, root, frame, username):
        self.root = root
        self.frame = frame
        self.username = username
        self.frame_empty = LabelFrame(self.frame, pady=250, padx=566)
        Label(self.frame_empty, text=" ").grid(row=1, column=1)
        self.frame_empty.grid(row=3, column=1)

        self.frame_442 = LabelFrame(self.frame, pady=5, padx=5)


        image = Image.open("back2.png")
        # Resize the image using resize() method
        resize_image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(resize_image)

        self.myFont2 = font.Font(family='Calibri', size=12)
        self.myFont3 = font.Font(family='Calibri', size=14, weight='bold')

        Button(self.frame, image=self.img, borderwidth=0, anchor=W, command=self.back).grid(row=0, column=0)

        Label(self.frame, text="\n").grid(row=1, column=0)

        options = ['4-4-2', '4-3-3', '3-5-2']

        clicked = StringVar()
        clicked.set("Select the type of formation")
        drop = OptionMenu(frame, clicked, *options, command=self.display_lineup)
        drop.grid(row=2, column=1)

        if clicked.get() == '4-4-2':
            print("ok")


