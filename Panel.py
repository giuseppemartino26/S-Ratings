from tkinter import *
import tkinter.font as font
from tkinter import messagebox

from Login import *
from Rating import Rating
from database import Database

db = Database()

class Panel:

    def check_team(self, name, role, username):
        stmt = "SELECT count(*) FROM players WHERE Name = %s AND Role = %s AND Username = %s"
        data = (name, role, username)
        db.mycursor.execute(stmt, data)

        result = db.mycursor.fetchall()
        if int(result[0][0]) >= 1:
            return True
        else:
            return False

    def add_player(self,name,role,username):
        if self.check_team(name,role, username):
            messagebox.showerror("Error", "The player is already present in the team")
        else:
            stmt = "INSERT INTO `soccer_ratings`.`players` (`Name`, `Role`, `Username`) VALUES (%s, %s, %s);"
            data = [name,role,username]
            db.mycursor.execute(stmt,data)
            messagebox.showinfo("Success","New player added in the team")


    def delete_player(self,player_name, username):
        stmt_delete = "DELETE from players where Name = %s and Username = %s"
        stmt_delete2 = "delete from performance where Player = %s and Username = %s"
        data_delete = [player_name,username]
        db.mycursor.execute(stmt_delete,data_delete)
        db.mycursor.execute(stmt_delete2,data_delete)
        messagebox.showinfo("Success", "Player deleted from your team")


    def __init__(self, root, frame, username):

        self.root = root
        self.frame = frame
        self.username = username

        self.frame_rating = LabelFrame(self.root, pady=5, padx=5)

        myFont = font.Font(family='Calibri', size=14)
        myFont2 = font.Font(family='Calibri', size=12)
        options = [
            "Goalkeeper",
            "Defensor",
            "Midfielder",
            "Forewarder"
        ]

        Label(frame, text="Modify your team:", font=myFont).grid(row=3, column=1)
        Label(frame, text=" ").grid(row=3,column=0)



        clicked = StringVar()
        clicked.set("Select a role")
        drop = OptionMenu(frame, clicked, *options)
        drop.grid(row=4,column=1)



        entry_insert_p = Entry(frame, width=25, font=myFont2)
        entry_insert_p.grid(row=4, column=2)
        button_insert_p = Button(frame, text="Insert new player", padx=25, pady=5, bg="#3bab5a", fg="white",font=myFont2,command=lambda: self.add_player(str(entry_insert_p.get()),str(clicked.get()), self.username))
        Label(frame, text="\n").grid(row=5, column=4)
        Button(frame, text="Delete a player", padx=25, pady=5, bg="#c80031", fg="white",
                                 font=myFont2,
                                 command=lambda: self.delete_player(clicked_mod.get(),self.username)).grid(row=6, column=4)

        stmt6 = "SELECT Name FROM players WHERE Username = %s"
        data_mod = [str(self.username)]
        db.mycursor.execute(stmt6, data_mod)
        result_mod = db.mycursor.fetchall()

        Label(frame,text=" ").grid(row=6, column=3)

        options_mod = []
        for player_mod in result_mod:
            options_mod.append(player_mod[0])
        global clicked_mod
        clicked_mod = StringVar()
        clicked_mod.set("Select the player to delete")
        drop_mod = OptionMenu(frame, clicked_mod, *options_mod)
        drop_mod.grid(row=6, column=2)




        space_label2 = Label(frame, text=" ")
        space_label3 = Label(frame, text="\n"+"\n")

        Label(frame, text=" ").grid(row=4,column=3)
        space_label2.grid(row=5,column=1)
        button_insert_p.grid(row=4,column=4)
        space_label3.grid(row=7, column=1)

        rating_button = Button(frame, text="Rate a player",padx=25, pady=10, bg="#1d434e", fg="white",font=myFont2, command=self.open_rating)
        rating_button.grid(row=8, column=2)
        space_label4 = Label(frame, text="\n" + "\n")
        space_label4.grid(row=9,column=1)

        lineup_button = Button(frame, text="View the starting lineup", padx=25, pady=10, bg="#1d434e", fg="white",font=myFont2)
        lineup_button.grid(row=10, column=2)
        space_label5 = Label(frame, text="\n" + "\n")
        space_label5.grid(row=11, column=1)


        trend_button = Button(frame, text="View a player's performance trend", padx=25, pady=10, bg="#1d434e", fg="white",font=myFont2,command= self.indietro)
        trend_button.grid(row=12, column=2)

    def indietro(self):
        self.frame.grid_forget()

    def open_rating(self):
        #self.frame.grid_forget()
        Rating(self.root, self.frame_rating, self.username)
        self.frame_rating.grid(row=2, column=1)











