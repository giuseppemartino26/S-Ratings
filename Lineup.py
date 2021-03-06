from database import Database
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox

db = Database()
global clicked

class Lineup:

    def back(self):
        #self.frame_mov.grid_forget()
        #self.frame_gk.grid_forget()
        self.frame.grid_forget()


    def compute_list(self, username, role, num):
        final_list = []
        stmt_p = "select p1.Player, avg(p1.rating) as avg_rating from Performance p1 where p1.role = %s and p1.Username = %s and (select count(*) from Performance p2 where p1.Player = p2.Player and p1.Date <= p2.Date) <=5 group by p1.Player"
        data_p = [role, username]
        db.mycursor.execute(stmt_p,data_p)
        result_p = db.mycursor.fetchall()
        sorted_result = sorted(result_p, key=lambda tup: tup[1], reverse=True)

        for i in range(num):
            try:
                final_list.append(sorted_result[i])
            except IndexError:
                messagebox.showerror("Impossible to compute the formation","You don't have enough rated players in all the roles of this type of formation.")
                return

        return final_list





    def display_lineup(self, choice):

        if choice == '4-4-2':
            self.frame_442.grid_forget()
            self.frame_352.grid_forget()
            fw_list = self.compute_list(self.username,'Foreward', 2)
            print(fw_list)

            Label(self.frame_442, image=self.img_g).place(anchor='center', relx=0.5, rely=0.5)

            Label(self.frame_442, text= fw_list[0][0] +"\n"+"("+ str(fw_list[0][1])+")",font=self.myFont2).grid(row=6, column=2)
            Label(self.frame_442, text= "        ",bg="#7ec576").grid(row=6,column=3)
            Label(self.frame_442, text=fw_list[1][0]+"\n"+"("+ str(fw_list[1][1])+")", font=self.myFont2).grid(row=6, column=4)

            Label(self.frame_442, text="\n"+"\n",bg="#7ec576").grid(row=5, column=0)

            mf_list = self.compute_list(self.username, 'Midfielder', 4)
            Label(self.frame_442, text=mf_list[0][0]+"\n"+"("+ str(mf_list[0][1])+")", font=self.myFont2).grid(row=4, column=0)
            Label(self.frame_442, text="        ",bg="#7ec576").grid(row=4, column=1)
            Label(self.frame_442, text=mf_list[1][0]+"\n"+"("+ str(mf_list[1][1])+")", font=self.myFont2).grid(row=4, column=2)
            Label(self.frame_442, text="        ",bg="#7ec576").grid(row=4, column=3)
            Label(self.frame_442, text=mf_list[2][0]+"\n"+"("+ str(mf_list[2][1])+")", font=self.myFont2).grid(row=4, column=4)
            Label(self.frame_442, text="        ",bg="#7ec576").grid(row=4, column=5)
            Label(self.frame_442, text=mf_list[3][0]+"\n"+"("+ str(mf_list[3][1])+")", font=self.myFont2).grid(row=4, column=6)

            Label(self.frame_442, text="\n" + "\n",bg="#7ec576").grid(row=3, column=0)

            df_list = self.compute_list(self.username, 'Defender', 4)
            Label(self.frame_442, text=df_list[0][0]+"\n"+"("+ str(df_list[0][1])+")", font=self.myFont2).grid(row=2, column=0)
            Label(self.frame_442, text="        ",bg="#7ec576").grid(row=2, column=1)
            Label(self.frame_442, text=df_list[1][0]+"\n"+"("+ str(df_list[1][1])+")", font=self.myFont2).grid(row=2, column=2)
            Label(self.frame_442, text="        ",bg="#7ec576").grid(row=2, column=3)
            Label(self.frame_442, text=df_list[2][0]+"\n"+"("+ str(df_list[2][1])+")", font=self.myFont2).grid(row=2, column=4)
            Label(self.frame_442, text="        ",bg="#7ec576").grid(row=2, column=5)
            Label(self.frame_442, text=df_list[3][0]+"\n"+"("+ str(df_list[3][1])+")", font=self.myFont2).grid(row=2, column=6)

            Label(self.frame_442, text="\n" + "\n",bg="#7ec576").grid(row=1, column=0)

            gk_list = self.compute_list(self.username, 'Goalkeeper', 1)
            Label(self.frame_442, text=gk_list[0][0]+"\n"+"("+ str(gk_list[0][1])+")", font=self.myFont2).grid(row=0, column=1, columnspan=5)


            self.frame_442.grid(row=3, column=1)
            self.frame_442.tkraise()


        if choice == '4-3-3':
            self.frame_442.grid_forget()
            self.frame_352.grid_forget()
            fw_list = self.compute_list(self.username,'Foreward', 3)
            print(fw_list)

            Label(self.frame_433, image=self.img_g).place(anchor='center', relx=0.5, rely=0.5)

            Label(self.frame_433, text= fw_list[0][0] +"\n"+"("+ str(fw_list[0][1])+")",font=self.myFont2).grid(row=6, column=1, columnspan=2)
            Label(self.frame_433, text=fw_list[1][0] + "\n" + "(" + str(fw_list[1][1]) + ")", font=self.myFont2).grid(row=6, column=2, columnspan=2)
            #Label(self.frame_442, text= "        ",bg="#7ec576").grid(row=6,column=3)
            Label(self.frame_433, text=fw_list[2][0]+"\n"+"("+ str(fw_list[2][1])+")", font=self.myFont2).grid(row=6, column=3, columnspan=2)

            Label(self.frame_433, text="\n"+"\n",bg="#7ec576").grid(row=5, column=0)

            mf_list = self.compute_list(self.username, 'Midfielder', 3)
            Label(self.frame_433, text=mf_list[0][0]+"\n"+"("+ str(mf_list[0][1])+")", font=self.myFont2).grid(row=4, column=1,columnspan=2)
            #Label(self.frame_442, text="        ",bg="#7ec576").grid(row=4, column=2)
            Label(self.frame_433, text=mf_list[1][0]+"\n"+"("+ str(mf_list[1][1])+")", font=self.myFont2).grid(row=4, column=2, columnspan=2)
            #Label(self.frame_442, text="        ",bg="#7ec576").grid(row=4, column=4)
            Label(self.frame_433, text=mf_list[2][0]+"\n"+"("+ str(mf_list[2][1])+")", font=self.myFont2).grid(row=4, column=3, columnspan=2)
            #Label(self.frame_442, text="        ",bg="#7ec576").grid(row=4, column=6)
            #abel(self.frame_442, text=mf_list[3][0]+"\n"+"("+ str(mf_list[3][1])+")", font=self.myFont2).grid(row=4, column=6)

            Label(self.frame_433, text="\n" + "\n",bg="#7ec576").grid(row=3, column=0)

            df_list = self.compute_list(self.username, 'Defender', 4)
            Label(self.frame_433, text=df_list[0][0]+"\n"+"("+ str(df_list[0][1])+")", font=self.myFont2).grid(row=2, column=1)
            #Label(self.frame_442, text="        ",bg="#7ec576").grid(row=2, column=1)
            Label(self.frame_433, text=df_list[1][0]+"\n"+"("+ str(df_list[1][1])+")", font=self.myFont2).grid(row=2, column=2)
            #Label(self.frame_442, text="        ",bg="#7ec576").grid(row=2, column=3)
            Label(self.frame_433, text=df_list[2][0]+"\n"+"("+ str(df_list[2][1])+")", font=self.myFont2).grid(row=2, column=3)
            #Label(self.frame_442, text="        ",bg="#7ec576").grid(row=2, column=5)
            Label(self.frame_433, text=df_list[3][0]+"\n"+"("+ str(df_list[3][1])+")", font=self.myFont2).grid(row=2, column=4)

            Label(self.frame_433, text="\n" + "\n",bg="#7ec576").grid(row=1, column=0)

            gk_list = self.compute_list(self.username, 'Goalkeeper', 1)
            Label(self.frame_433, text=gk_list[0][0]+"\n"+"("+ str(gk_list[0][1])+")", font=self.myFont2).grid(row=0, column=2, columnspan=2)


            self.frame_433.grid(row=3, column=1)
            self.frame_433.tkraise()


        if choice == '3-5-2':
            self.frame_442.grid_forget()
            self.frame_433.grid_forget()
            fw_list = self.compute_list(self.username,'Foreward', 2)


            Label(self.frame_352, image=self.img_g).place(anchor='center', relx=0.5, rely=0.5)

            Label(self.frame_352, text= fw_list[0][0] +"\n"+"("+ str(fw_list[0][1])+")",font=self.myFont2).grid(row=6, column=0, columnspan=2)
            Label(self.frame_352, text=fw_list[1][0] + "\n" + "(" + str(fw_list[1][1]) + ")", font=self.myFont2).grid(row=6, column=4, columnspan=2)


            Label(self.frame_352, text="\n"+"\n"+"\n"+"\n"+"\n",bg="#7ec576").grid(row=5, column=0)

            mf_list = self.compute_list(self.username, 'Midfielder', 5)
            Label(self.frame_352, text=mf_list[0][0]+"\n"+"("+ str(mf_list[0][1])+")", font=self.myFont2).grid(row=4, column=0)

            Label(self.frame_352, text=mf_list[1][0]+"\n"+"("+ str(mf_list[1][1])+")", font=self.myFont2).grid(row=4, column=2)

            Label(self.frame_352, text=mf_list[2][0]+"\n"+"("+ str(mf_list[2][1])+")", font=self.myFont2).grid(row=4, column=4)

            Label(self.frame_352, text=mf_list[3][0] + "\n" + "(" + str(mf_list[3][1]) + ")", font=self.myFont2).grid(row=5, column=0, columnspan=2)
            Label(self.frame_352, text=mf_list[4][0] + "\n" + "(" + str(mf_list[4][1]) + ")", font=self.myFont2).grid(row=5, column=4, columnspan=2)


            Label(self.frame_352, text="\n" + "\n",bg="#7ec576").grid(row=3, column=0)

            df_list = self.compute_list(self.username, 'Defender',3)
            Label(self.frame_352, text=df_list[0][0]+"\n"+"("+ str(df_list[0][1])+")", font=self.myFont2).grid(row=2, column=0)
            Label(self.frame_442, text="  ", bg="#7ec576").grid(row=2, column=1)
            Label(self.frame_352, text=df_list[1][0]+"\n"+"("+ str(df_list[1][1])+")", font=self.myFont2).grid(row=2, column=2)
            Label(self.frame_442, text="  ", bg="#7ec576").grid(row=2, column=2)
            Label(self.frame_352, text=df_list[2][0]+"\n"+"("+ str(df_list[2][1])+")", font=self.myFont2).grid(row=2, column=4)


            Label(self.frame_352, text="\n" + "\n",bg="#7ec576").grid(row=1, column=0)

            gk_list = self.compute_list(self.username, 'Goalkeeper', 1)
            Label(self.frame_352, text=gk_list[0][0]+"\n"+"("+ str(gk_list[0][1])+")", font=self.myFont2).grid(row=0, column=2)


            self.frame_352.grid(row=3, column=1)
            self.frame_352.tkraise()








    def __init__(self, root, frame, username):
        self.root = root
        self.frame = frame
        self.username = username
        self.frame_empty = LabelFrame(self.frame, pady=250, padx=566)
        Label(self.frame_empty, text=" ").grid(row=1, column=1)
        self.frame_empty.grid(row=3, column=1)

        self.frame_442 = LabelFrame(self.frame, pady=90, padx=5)
        self.frame_433 = LabelFrame(self.frame, pady=90, padx=25)
        self.frame_352 = LabelFrame(self.frame, pady=70, padx=100)


        image = Image.open("back2.png")
        # Resize the image using resize() method
        resize_image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(resize_image)

        image_ground = Image.open("ground.png")
        # Resize the image using resize() method
        resize_image_g = image_ground.resize((680, 680))
        self.img_g = ImageTk.PhotoImage(resize_image_g)

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


