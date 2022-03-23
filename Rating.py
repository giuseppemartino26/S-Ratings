from datetime import datetime
from tkinter import *
import tkinter.font as font
from tkinter import ttk

from PIL import ImageTk, Image

from database import Database
import pickle
from tkinter import messagebox
from sklearn import model_selection


db = Database()


class Rating:

    def __init__(self, root, frame, username):
        self.root = root
        self.frame = frame
        self.username = username
        self.frame_empty = LabelFrame(self.frame, pady=250, padx=566)
        Label(self.frame_empty, text=" ").grid(row=1, column=1)
        self.frame_empty.grid(row=3, column=1)

        self.model = pickle.load(open('model_mov.sav', 'rb'))

        self.frame_gk = LabelFrame(self.frame, pady=5, padx=5)
        self.frame_mov = LabelFrame(self.frame, pady=5, padx=5)

        self.my_canvas = Canvas(self.frame_mov, width=1100, height=500)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = ttk.Scrollbar(self.frame_mov, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        self.second_frame = Frame(self.my_canvas)
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        image = Image.open("back2.png")
        # Resize the image using resize() method
        resize_image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(resize_image)

        self.myFont2 = font.Font(family='Calibri', size=12)
        self.myFont3 = font.Font(family='Calibri', size=14, weight='bold')

        Button(self.frame, image=self.img, borderwidth=0, anchor=W, command=self.back).grid(row=0, column=0)

        Label(self.frame, text="\n").grid(row=1, column=0)

        """Label(self.frame,text="Is the player a goalkeeper?",font=myFont2).grid(row=2,column=1)
        global var
        var = IntVar()
        Radiobutton(self.frame,text="Yes",variable=var, value=1,font=myFont2).grid(row=2,column=2)
        Radiobutton(self.frame, text="No", variable=var, value=0,font=myFont2,command=self.display_mov).grid(row=2, column=3)"""

        stmt = "SELECT Name FROM teams WHERE Username = %s"
        data_user = [str(self.username)]
        db.mycursor.execute(stmt,data_user)
        result = db.mycursor.fetchall()
        # print(result)

        options = []
        for player in result:
            options.append(player[0])
        global clicked
        clicked = StringVar()
        clicked.set("Select the player")
        drop = OptionMenu(frame, clicked, *options, command=self.select_player)
        drop.grid(row=2, column=1)

    def select_player(self, choice):
        choice = str(clicked.get())
        stmt2 = "SELECT Role FROM teams WHERE Name = %s"
        data2 = [choice]
        db.mycursor.execute(stmt2, data2)
        result2 = db.mycursor.fetchall()
        role = result2[0][0]
        # print(role)
        if role == 'Goalkeeper':
            self.display_gk()
        elif role == 'Defender':
            self.display_mov(1,choice,role)
        else:
            self.display_mov(0,choice,role)

    def back(self):
        self.frame.grid_forget()

    def display_gk(self):
        Label(self.frame_gk, text="Assists",font=self.myFont2).grid(row=0, column=0)
        assists = Entry(self.frame_gk, width=5, font=self.myFont2)
        assists.grid(row=1, column=0)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=0, column=1)

        Label(self.frame_gk, text="Ground duels won", font=self.myFont2).grid(row=0, column=2)
        grduels_w = Entry(self.frame_gk, width=5, font=self.myFont2)
        grduels_w.grid(row=1, column=2)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=0, column=3)

        Label(self.frame_gk, text="Ground duels lost", font=self.myFont2).grid(row=0, column=4)
        grduels_l = Entry(self.frame_gk, width=5, font=self.myFont2)
        grduels_l.grid(row=1, column=4)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=0, column=5)

        Label(self.frame_gk, text="Aerials won", font=self.myFont2).grid(row=0, column=6)
        aerials_w = Entry(self.frame_gk, width=5, font=self.myFont2)
        aerials_w.grid(row=1, column=6)

        Label(self.frame_gk, text="\n"+"\n"+"\n"+"\n").grid(row=2, column=1)

        Label(self.frame_gk, text="Aerials lost", font=self.myFont2).grid(row=3, column=0)
        aerials_l = Entry(self.frame_gk, width=5, font=self.myFont2)
        aerials_l.grid(row=4, column=0)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=3, column=1)

        Label(self.frame_gk, text="Dangerous mistakes", font=self.myFont2).grid(row=3, column=2)
        d_mistakes = Entry(self.frame_gk, width=5, font=self.myFont2)
        d_mistakes.grid(row=4, column=2)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=3, column=3)

        Label(self.frame_gk, text="Goals against"+"\n"+"outside the box", font=self.myFont2).grid(row=3, column=4)
        goals_ag_otb = Entry(self.frame_gk, width=5, font=self.myFont2)
        goals_ag_otb.grid(row=4, column=4)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=3, column=5)

        Label(self.frame_gk, text="Goals against" + "\n" + "inside the box", font=self.myFont2).grid(row=3, column=6)
        goals_ag_itb = Entry(self.frame_gk, width=5, font=self.myFont2)
        goals_ag_itb.grid(row=4, column=6)

        Label(self.frame_gk, text="\n"+"\n"+"\n"+"\n").grid(row=5, column=1)

        Label(self.frame_gk, text="Saves inside the box", font=self.myFont2).grid(row=6, column=0)
        saves_itb = Entry(self.frame_gk, width=5, font=self.myFont2)
        saves_itb.grid(row=7, column=0)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=6, column=1)

        Label(self.frame_gk, text="Saves outside the box", font=self.myFont2).grid(row=6, column=2)
        saves_otb = Entry(self.frame_gk, width=5, font=self.myFont2)
        saves_otb.grid(row=7, column=2)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=6, column=3)

        Label(self.frame_gk, text="Saved penalties", font=self.myFont2).grid(row=6, column=4)
        saves_otb = Entry(self.frame_gk, width=5, font=self.myFont2)
        saves_otb.grid(row=7, column=4)

        Label(self.frame_gk,
              text="                                                    ").grid(
            row=6, column=5)

        Label(self.frame_gk, text="Betweennes centrality", font=self.myFont2).grid(row=6, column=6)
        betweennes_centrality = Entry(self.frame_gk, width=10, font=self.myFont2)
        betweennes_centrality.grid(row=7, column=6)




        self.frame_mov.grid_forget()
        self.frame_gk.grid(row=3, column=1)
        self.frame_gk.tkraise()

    def display_mov(self, defender, choice, role):

        self.frame_mov.forget()

        Label(self.second_frame, text="Goals", font=self.myFont2).grid(row=0, column=0)
        goals = Entry(self.second_frame, width=5, font=self.myFont2)
        goals.grid(row=1, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=1, column=1)

        Label(self.second_frame, text="Assists", font=self.myFont2).grid(row=0, column=2)
        assists = Entry(self.second_frame, width=5, font=self.myFont2)
        assists.grid(row=1, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=1, column=3)

        Label(self.second_frame, text="Shots on target", font=self.myFont2).grid(row=0, column=4)
        shotsont = Entry(self.second_frame, width=5, font=self.myFont2)
        shotsont.grid(row=1, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=1, column=5)

        Label(self.second_frame, text="Chances to score", font=self.myFont2).grid(row=0, column=6)
        chances2sc = Entry(self.second_frame, width=5, font=self.myFont2)
        chances2sc.grid(row=1, column=6)

        Label(self.second_frame, text="\n").grid(row=2, column=1)

        Label(self.second_frame, text="Dribblings", font=self.myFont2).grid(row=3, column=0)
        dribblings = Entry(self.second_frame, width=5, font=self.myFont2)
        dribblings.grid(row=4, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=3, column=1)

        Label(self.second_frame, text="Touches", font=self.myFont2).grid(row=3, column=2)
        touches = Entry(self.second_frame, width=5, font=self.myFont2)
        touches.grid(row=4, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=3, column=3)

        Label(self.second_frame, text="Accurated passes", font=self.myFont2).grid(row=3, column=4)
        passes_acc = Entry(self.second_frame, width=5, font=self.myFont2)
        passes_acc.grid(row=4, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=3, column=5)

        Label(self.second_frame, text="Inaccurated passes", font=self.myFont2).grid(row=3, column=6)
        passes_inacc = Entry(self.second_frame, width=5, font=self.myFont2)
        passes_inacc.grid(row=4, column=6)

        Label(self.second_frame, text="\n").grid(row=5, column=1)

        Label(self.second_frame, text="Accurated long passes", font=self.myFont2).grid(row=6, column=0)
        lballs_acc = Entry(self.second_frame, width=5, font=self.myFont2)
        lballs_acc.grid(row=7, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=7, column=1)

        Label(self.second_frame, text="Inaccurated long passes", font=self.myFont2).grid(row=6, column=2)
        lballs_inacc = Entry(self.second_frame, width=5, font=self.myFont2)
        lballs_inacc.grid(row=7, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=7, column=3)

        Label(self.second_frame, text="Ground duels won", font=self.myFont2).grid(row=6, column=4)
        grduels_w = Entry(self.second_frame, width=5, font=self.myFont2)
        grduels_w.grid(row=7, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=7, column=5)

        Label(self.second_frame, text="Aerials won", font=self.myFont2).grid(row=6, column=6)
        aerials_w = Entry(self.second_frame, width=5, font=self.myFont2)
        aerials_w.grid(row=7, column=6)

        Label(self.second_frame, text="\n").grid(row=8, column=1)

        Label(self.second_frame, text="Possession lost", font=self.myFont2).grid(row=9, column=0)
        poss_lost = Entry(self.second_frame, width=5, font=self.myFont2)
        poss_lost.grid(row=10, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=10, column=1)

        Label(self.second_frame, text="Clearances", font=self.myFont2).grid(row=9, column=2)
        clearances = Entry(self.second_frame, width=5, font=self.myFont2)
        clearances.grid(row=10, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=10, column=3)

        Label(self.second_frame, text="Interceptions", font=self.myFont2).grid(row=9, column=4)
        interceptions = Entry(self.second_frame, width=5, font=self.myFont2)
        interceptions.grid(row=10, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=10, column=5)

        Label(self.second_frame, text="Tackles", font=self.myFont2).grid(row=9, column=6)
        tackles = Entry(self.second_frame, width=5, font=self.myFont2)
        tackles.grid(row=10, column=6)

        Label(self.second_frame, text="\n").grid(row=11, column=1)

        var = IntVar()
        rcards = Checkbutton(self.second_frame, text="Red Cards", font=self.myFont2, variable=var, onvalue=1,
                             offvalue=0)
        rcards.grid(row=12, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=12, column=1)

        Label(self.second_frame, text="# Counter attacks", font=self.myFont2).grid(row=12, column=2)
        countattack = Entry(self.second_frame, width=5, font=self.myFont2)
        countattack.grid(row=13, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=12, column=3)

        Label(self.second_frame, text="Betweenness" + "\n" + "centrality", font=self.myFont2).grid(row=12, column=4)
        betweenness_centrality = Entry(self.second_frame, width=5, font=self.myFont2)
        betweenness_centrality.grid(row=13, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=12, column=5)

        Label(self.second_frame, text="Closeness" + "\n" + "centrality", font=self.myFont2).grid(row=12, column=6)
        closeness_centrality = Entry(self.second_frame, width=5, font=self.myFont2)
        closeness_centrality.grid(row=13, column=6)

        Label(self.second_frame, text="\n").grid(row=14, column=1)

        Label(self.second_frame, text="Flow" + "\n" + "centrality", font=self.myFont2).grid(row=15, column=0)
        flow_centrality = Entry(self.second_frame, width=5, font=self.myFont2)
        flow_centrality.grid(row=16, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=15, column=1)

        Label(self.second_frame, text="Flow" + "\n" + "success", font=self.myFont2).grid(row=15, column=2)
        flow_success = Entry(self.second_frame, width=5, font=self.myFont2)
        flow_success.grid(row=16, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=15, column=3)

        Label(self.second_frame, text="Betweenness" + "\n" + "to goals", font=self.myFont2).grid(row=15, column=4)
        betweenness2goals = Entry(self.second_frame, width=5, font=self.myFont2)
        betweenness2goals.grid(row=16, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=15, column=5)

        win_var = IntVar()
        win = Checkbutton(self.second_frame, text="Win", font=self.myFont2, variable=win_var, onvalue=1,
                          offvalue=0)
        win.grid(row=15, column=6)

        lost_var = IntVar()
        lost = Checkbutton(self.second_frame, text="Lost", font=self.myFont2, variable=lost_var, onvalue=1,
                           offvalue=0)
        lost.grid(row=16, column=6)

        Label(self.second_frame, text="\n").grid(row=17, column=1)

        Label(self.second_frame, text="Minutes played", font=self.myFont2).grid(row=18, column=0)
        minutes_played = Entry(self.second_frame, width=5, font=self.myFont2)
        minutes_played.grid(row=19, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=18, column=1)

        Label(self.second_frame, text="Starter", font=self.myFont2).grid(row=18, column=2)
        starter = Entry(self.second_frame, width=5, font=self.myFont2)
        starter.grid(row=19, column=2)

        Label(self.second_frame,
              text="\n" + "\n" + "\n" + "\n" + "\n" + "\n").grid(
            row=19, column=1)

        Button(self.second_frame, text="Compute the rating", font=self.myFont3, padx=25, pady=5, bg="#3bab5a",
               fg="white", command=lambda: self.compute_rating(int(goals.get()),
                                                               int(assists.get()), int(shotsont.get()),
                                                               int(chances2sc.get()), int(dribblings.get()),
                                                               int(touches.get()), int(passes_acc.get()),
                                                               int(passes_inacc.get()), int(lballs_acc.get()),
                                                               int(lballs_inacc.get()), int(grduels_w.get()),
                                                               int(aerials_w.get()), int(poss_lost.get()),
                                                               int(clearances.get()), int(interceptions.get()),
                                                               int(tackles.get()), var.get(),
                                                               int(countattack.get()),
                                                               float(betweenness_centrality.get()),
                                                               float(closeness_centrality.get()),
                                                               float(flow_centrality.get()), float(flow_success.get()),
                                                               float(betweenness2goals.get()), win_var.get(),
                                                               lost_var.get(), int(minutes_played.get()),
                                                               int(starter.get()), defender, choice, role)).grid(row=20, column=3)

        self.frame_mov.grid(row=3, column=1)
        self.frame_mov.tkraise()

    def compute_rating(self, goals, assists, shotsont, chances2c, dribblings, touches, passes_acc, passes_inacc,
                       lballs_acc, lballs_inacc, grduels_w, aerials_w, poss_lost_w, clearances, interceptions, tackles,
                       rcards, countattack, b_centrality, closeness_centrality, flow_centrality, flow_success, b2goals,
                       win, lost, minutes_played, starter, DF, choice, role):
        input_data = [[goals, assists, shotsont, chances2c, dribblings, touches, passes_acc, passes_inacc,
                       lballs_acc, lballs_inacc, grduels_w, aerials_w, poss_lost_w, clearances, interceptions, tackles,
                       rcards, countattack, b_centrality, closeness_centrality, flow_centrality, flow_success, b2goals,
                       win, lost, minutes_played, starter, DF]]
        #input_data = [[3,0,0,0,0,34,20,5,5,1,0,2,11,8,3,0,0,2,0.143055419,0.603571429,0.304347826,0,0,0,1,90,1,0]]

        result = self.model.predict(input_data)

        text_final = f"The rating is {result[0]}"

        messagebox.showinfo("Rating result", text_final)

        stmt5 = "INSERT INTO soccer_ratings.performance (`Username`, `Player`, `Date`, `rating`, `role`) VALUES (%s, %s, %s, %s, %s) "
        data_insert = [self.username, choice, datetime.date(datetime.now()), int(result[0]), role]
        db.mycursor.execute(stmt5,data_insert)










