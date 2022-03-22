from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image

from database import Database

db = Database()


class Rating:

    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.frame_empty = LabelFrame(self.frame, pady=250, padx=350)
        Label(self.frame_empty,text=" ").grid(row=1,column=1)
        self.frame_empty.grid(row=3,column=1)


        self.frame_gk = LabelFrame(self.frame, pady=5, padx=5)
        self.frame_mov = LabelFrame(self.frame, pady=5, padx=5)

        image = Image.open("back2.png")
        # Resize the image using resize() method
        resize_image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(resize_image)

        self.myFont2 = font.Font(family='Calibri', size=12)

        Button(self.frame, image=self.img, borderwidth=0, anchor=W, command=self.back).grid(row=0, column=0)

        Label(self.frame, text="\n").grid(row=1, column=0)

        """Label(self.frame,text="Is the player a goalkeeper?",font=myFont2).grid(row=2,column=1)
        global var
        var = IntVar()
        Radiobutton(self.frame,text="Yes",variable=var, value=1,font=myFont2).grid(row=2,column=2)
        Radiobutton(self.frame, text="No", variable=var, value=0,font=myFont2,command=self.display_mov).grid(row=2, column=3)"""

        stmt = "SELECT Name FROM teams"
        db.mycursor.execute(stmt)
        result = db.mycursor.fetchall()
        # print(result)

        options = []
        for player in result:
            options.append(player[0])
        global clicked
        clicked = StringVar()
        clicked.set("Select the player")
        drop = OptionMenu(frame, clicked, *options, command= self.select_player)
        drop.grid(row=2, column=1)


    def select_player(self,choice):
        choice = str(clicked.get())
        stmt2 = "SELECT Role FROM teams WHERE Name = %s"
        data2 = [choice]
        db.mycursor.execute(stmt2, data2)
        result2 = db.mycursor.fetchall()
        role = result2[0][0]
        #print(role)
        if role == 'Goalkeeper':
            self.display_gk()
        else:
            self.display_mov()




    def back(self):
        self.frame.grid_forget()

    def display_gk(self):
        Label(self.frame_gk, text="Goals").grid(row=0, column=0)
        Label(self.frame_gk, text="                                                                                                                ").grid(row=0, column=1)
        Label(self.frame_gk, text="Assists ").grid(row=0, column=2)
        Label(self.frame_gk, text="                                                                                                                ").grid(row=0, column=3)
        Label(self.frame_gk, text="fouls").grid(row=0, column=4)
        #Label(self.frame_gk, text="\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"Goals").grid(row=1, column=0)

        #Label(self.frame_gk, text="                                                                                                                                              Goals").grid(row=1, column=0)

        self.frame_gk.grid(row=3, column=1)
        self.frame_gk.tkraise()

    def display_mov(self):
        Label(self.frame_mov, text="Goals", font=self.myFont2).grid(row=0, column=0)
        goals = Entry(self.frame_mov,width=5,font=self.myFont2).grid(row=1,column=0)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=1, column=1)

        Label(self.frame_mov, text="Assists", font=self.myFont2).grid(row=0, column=2)
        assists = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=1, column=2)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=1, column=3)

        Label(self.frame_mov, text="Shots on target", font=self.myFont2).grid(row=0, column=4)
        shotsont = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=1, column=4)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=1, column=5)

        Label(self.frame_mov, text="Chances to score", font=self.myFont2).grid(row=0, column=6)
        chances2sc = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=1, column=6)

        Label(self.frame_mov, text="\n").grid(row=2,column=1)

        Label(self.frame_mov, text="Dribblings", font=self.myFont2).grid(row=3, column=0)
        dribblings = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=4, column=0)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=3, column=1)

        Label(self.frame_mov, text="Touches", font=self.myFont2).grid(row=3, column=2)
        touches = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=4, column=2)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=3, column=3)

        Label(self.frame_mov, text="Accurated passes", font=self.myFont2).grid(row=3, column=4)
        passes_acc = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=4, column=4)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=3, column=5)

        Label(self.frame_mov, text="Inaccurated passes", font=self.myFont2).grid(row=3, column=6)
        passes_inacc = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=4, column=6)

        Label(self.frame_mov, text="\n").grid(row=5, column=1)

        Label(self.frame_mov, text="Accurated long passes", font=self.myFont2).grid(row=6, column=0)
        lballs_acc = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=7, column=0)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=7, column=1)

        Label(self.frame_mov, text="Inaccurated long passes", font=self.myFont2).grid(row=6, column=2)
        lballs_inacc = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=7, column=2)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=7, column=3)

        Label(self.frame_mov, text="Ground duels won", font=self.myFont2).grid(row=6, column=4)
        grduels_w = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=7, column=4)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=7, column=5)

        Label(self.frame_mov, text="Aerials won", font=self.myFont2).grid(row=6, column=6)
        aerials_w = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=7, column=6)

        Label(self.frame_mov, text="\n").grid(row=8, column=1)

        Label(self.frame_mov, text="Possession lost", font=self.myFont2).grid(row=9, column=0)
        poss_lost = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=10, column=0)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=10, column=1)

        Label(self.frame_mov, text="Clearances", font=self.myFont2).grid(row=9, column=2)
        clearances = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=10, column=2)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=10, column=3)

        Label(self.frame_mov, text="Interceptions", font=self.myFont2).grid(row=9, column=4)
        interceptions = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=10, column=4)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=10, column=5)

        Label(self.frame_mov, text="Tackles", font=self.myFont2).grid(row=9, column=6)
        tackles = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=10, column=6)

        Label(self.frame_mov, text="\n").grid(row=11, column=1)

        var = IntVar()
        rcards = Checkbutton(self.frame_mov, text="Red Cards",font=self.myFont2, variable= var, onvalue=1, offvalue=0)
        rcards.grid(row=12, column=0)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=12, column=1)

        Label(self.frame_mov, text="# Counter attacks", font=self.myFont2).grid(row=12, column=2)
        countattack = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=13, column=2)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=12, column=3)

        Label(self.frame_mov, text="Betweenness"+"\n"+"centrality", font=self.myFont2).grid(row=12, column=4)
        betweenness_centrality = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=13, column=4)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=12, column=5)

        Label(self.frame_mov, text="Closeness" + "\n" + "centrality", font=self.myFont2).grid(row=12, column=6)
        closeness_centrality = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=13, column=6)

        Label(self.frame_mov, text="\n").grid(row=14, column=1)

        Label(self.frame_mov, text="Flow" + "\n" + "centrality", font=self.myFont2).grid(row=15, column=0)
        flow_centrality = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=16, column=0)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=15, column=1)

        Label(self.frame_mov, text="Flow" + "\n" + "success", font=self.myFont2).grid(row=15, column=2)
        flow_success = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=16, column=2)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=15, column=3)

        Label(self.frame_mov, text="Betweenness" + "\n" + "to goals", font=self.myFont2).grid(row=15, column=4)
        betweenness2goals = Entry(self.frame_mov, width=5, font=self.myFont2).grid(row=16, column=4)

        Label(self.frame_mov,
              text="                                                    ").grid(
            row=15, column=5)






        self.frame_mov.grid(row=3, column=1)
        self.frame_mov.tkraise()
