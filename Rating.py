
from tkinter import *
import tkinter.font as font
from tkinter import ttk


from PIL import ImageTk, Image

from database import Database
import pickle
from tkinter import messagebox
from tkcalendar import DateEntry



db = Database()


class Rating:

    def __init__(self, root, frame, username):
        self.root = root
        self.frame = frame
        self.username = username
        self.frame_empty = LabelFrame(self.frame, pady=250, padx=566)
        Label(self.frame_empty, text=" ").grid(row=1, column=1)

        self.model = pickle.load(open('model_mov.sav', 'rb'))
        self.model_gk = pickle.load(open('model_gk.sav', 'rb'))

        self.frame_gk = LabelFrame(self.frame, pady=5, padx=5)
        self.frame_mov = LabelFrame(self.frame, pady=5, padx=5)

        self.frame_empty.grid(row=3, column=1)
        self.frame_gk.grid_forget()
        self.frame_mov.grid_forget()

        self.my_canvas = Canvas(self.frame_mov, width=1100, height=500)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = ttk.Scrollbar(self.frame_mov, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        self.second_frame = Frame(self.my_canvas)
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")


        ###############################################################################################################################
        self.my_canvas2 = Canvas(self.frame_gk, width=1100, height=500)
        self.my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar2 = ttk.Scrollbar(self.frame_gk, orient=VERTICAL, command=self.my_canvas2.yview)
        self.my_scrollbar2.pack(side=RIGHT, fill=Y)

        self.my_canvas2.configure(yscrollcommand=self.my_scrollbar2.set)
        self.my_canvas2.bind('<Configure>', lambda e: self.my_canvas2.configure(scrollregion=self.my_canvas2.bbox("all")))

        self.third_frame = Frame(self.my_canvas2)
        self.my_canvas2.create_window((0, 0), window=self.third_frame, anchor="nw")












        image = Image.open("back2.png")
        # Resize the image using resize() method
        resize_image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(resize_image)

        self.myFont2 = font.Font(family='Calibri', size=12)
        self.myFont3 = font.Font(family='Calibri', size=14, weight='bold')

        Button(self.frame, image=self.img, borderwidth=0, anchor=W, command=self.back).grid(row=0, column=0)

        Label(self.frame, text="\n").grid(row=1, column=0)



        stmt = "SELECT Name FROM players WHERE Username = %s"
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
        stmt2 = "SELECT Role FROM players WHERE Name = %s"
        data2 = [choice]
        db.mycursor.execute(stmt2, data2)
        result2 = db.mycursor.fetchall()
        role = result2[0][0]
        # print(role)
        if role == 'Goalkeeper':
            self.frame_mov.grid_forget()
            self.frame_empty.grid_forget()
            self.display_gk(choice, role)
        else:
            self.frame_gk.grid_forget()
            self.frame_empty.grid_forget()
            self.display_mov(choice,role)

    def back(self):
        self.frame_mov.grid_forget()
        self.frame_gk.grid_forget()
        self.frame.grid_forget()

    def display_gk(self, choice, role):
        Label(self.third_frame, text="Goals", font=self.myFont2).grid(row=0, column=2)
        goals = Entry(self.third_frame, width=5, font=self.myFont2)
        goals.grid(row=1, column=2)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=1, column=1)

        Label(self.third_frame, text="Assists", font=self.myFont2).grid(row=0, column=4)
        assists = Entry(self.third_frame, width=5, font=self.myFont2)
        assists.grid(row=1, column=4)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=1, column=3)

        Label(self.third_frame, text="Shots on target", font=self.myFont2).grid(row=12, column=0)
        shotsont = Entry(self.third_frame, width=5, font=self.myFont2)
        shotsont.grid(row=13, column=0)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=1, column=5)

        Label(self.third_frame, text="Key passes", font=self.myFont2).grid(row=0, column=6)
        keypasses = Entry(self.third_frame, width=5, font=self.myFont2)
        keypasses.grid(row=1, column=6)

        Label(self.third_frame, text="\n").grid(row=2, column=1)

        Label(self.third_frame, text="Dribblings", font=self.myFont2).grid(row=3, column=0)
        dribblings = Entry(self.third_frame, width=5, font=self.myFont2)
        dribblings.grid(row=4, column=0)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=3, column=1)

        Label(self.third_frame, text="Touches", font=self.myFont2).grid(row=3, column=2)
        touches = Entry(self.third_frame, width=5, font=self.myFont2)
        touches.grid(row=4, column=2)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=3, column=3)

        Label(self.third_frame, text="Accurated passes", font=self.myFont2).grid(row=3, column=4)
        passes_acc = Entry(self.third_frame, width=5, font=self.myFont2)
        passes_acc.grid(row=4, column=4)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=3, column=5)

        Label(self.third_frame, text="Accurated crosses", font=self.myFont2).grid(row=3, column=6)
        crosses_acc = Entry(self.third_frame, width=5, font=self.myFont2)
        crosses_acc.grid(row=4, column=6)

        Label(self.third_frame, text="\n").grid(row=5, column=1)

        Label(self.third_frame, text="Accurated long passes", font=self.myFont2).grid(row=6, column=0)
        lballs_acc = Entry(self.third_frame, width=5, font=self.myFont2)
        lballs_acc.grid(row=7, column=0)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=7, column=1)

        Label(self.third_frame, text="Stopped shots", font=self.myFont2).grid(row=6, column=2)
        stop_shots = Entry(self.third_frame, width=5, font=self.myFont2)
        stop_shots.grid(row=7, column=2)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=7, column=3)

        Label(self.third_frame, text="Ground duels won", font=self.myFont2).grid(row=6, column=4)
        grduels_w = Entry(self.third_frame, width=5, font=self.myFont2)
        grduels_w.grid(row=7, column=4)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=7, column=5)

        Label(self.third_frame, text="Aerials won", font=self.myFont2).grid(row=6, column=6)
        aerials_w = Entry(self.third_frame, width=5, font=self.myFont2)
        aerials_w.grid(row=7, column=6)

        Label(self.third_frame, text="\n").grid(row=8, column=1)

        Label(self.third_frame, text="Possession lost", font=self.myFont2).grid(row=9, column=0)
        poss_lost = Entry(self.third_frame, width=5, font=self.myFont2)
        poss_lost.grid(row=10, column=0)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=10, column=1)

        Label(self.third_frame, text="Clearances", font=self.myFont2).grid(row=9, column=2)
        clearances = Entry(self.third_frame, width=5, font=self.myFont2)
        clearances.grid(row=10, column=2)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=10, column=3)

        Label(self.third_frame, text="Interceptions", font=self.myFont2).grid(row=9, column=4)
        interceptions = Entry(self.third_frame, width=5, font=self.myFont2)
        interceptions.grid(row=10, column=4)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=10, column=5)

        Label(self.third_frame, text="Tackles", font=self.myFont2).grid(row=9, column=6)
        tackles = Entry(self.third_frame, width=5, font=self.myFont2)
        tackles.grid(row=10, column=6)

        Label(self.third_frame, text="\n").grid(row=11, column=1)

        var = IntVar()
        rcards = Checkbutton(self.third_frame, text="Red Cards", font=self.myFont2, variable=var, onvalue=1,
                             offvalue=0)
        rcards.grid(row=18, column=0)

        Label(self.third_frame, text="saves inside"+"\n"+"the box", font=self.myFont2).grid(row=15, column=0)
        saves_itb = Entry(self.third_frame, width=5, font=self.myFont2)
        saves_itb.grid(row=16, column=0)

        Label(self.third_frame, text="saves outside"+"\n"+"the box", font=self.myFont2).grid(row=15, column=2)
        saves_otb = Entry(self.third_frame, width=5, font=self.myFont2)
        saves_otb.grid(row=16, column=2)

        varyellow = IntVar()
        ycards = Checkbutton(self.third_frame, text="Yellow Cards", font=self.myFont2, variable=varyellow, onvalue=1,
                             offvalue=0)
        ycards.grid(row=19, column=0)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=12, column=1)

        Label(self.third_frame, text="Own goals", font=self.myFont2).grid(row=12, column=2)
        owngoals = Entry(self.third_frame, width=5, font=self.myFont2)
        owngoals.grid(row=13, column=2)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=12, column=3)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=12, column=5)

        Label(self.third_frame, text="\n").grid(row=14, column=1)

        Label(self.third_frame, text="# actions in which" + "\n" + "player is involved", font=self.myFont2).grid(row=12, column=4)
        actions_involved = Entry(self.third_frame, width=10, font=self.myFont2)
        actions_involved.grid(row=13, column=4)

        Label(self.third_frame, text="Goals against"+"\n"+"outside the box", font=self.myFont2).grid(row=15, column=4)
        goals_ag_otb = Entry(self.third_frame, width=5, font=self.myFont2)
        goals_ag_otb.grid(row=16, column=4)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=15, column=1)

        Label(self.third_frame, text="Select the date of the match").grid(row=0, column=0)
        cal_mov = DateEntry(self.third_frame, width=12, year=2022, month=4, day=11, background='darkblue',
                            foreground='white', borderwidth=2)
        cal_mov.grid(row=1, column=0)

        Label(self.third_frame, text="# actions which end with"+"\n"+"a shot where"+"\n"+ "player is involved", font=self.myFont2).grid(row=12, column=6)
        actions_shot = Entry(self.third_frame, width=10, font=self.myFont2)
        actions_shot.grid(row=13, column=6)

        Label(self.third_frame, text="# Total actions of the team",
              font=self.myFont2).grid(row=18, column=4)
        actions_total = Entry(self.third_frame, width=10, font=self.myFont2)
        actions_total.grid(row=19, column=4)

        Label(self.third_frame, text="Goals against" + "\n" + "inside the box", font=self.myFont2).grid(row=15,column=6)
        goals_ag_itb = Entry(self.third_frame, width=5, font=self.myFont2)
        goals_ag_itb.grid(row=16, column=6)

        Label(self.third_frame, text="saved penalties", font=self.myFont2).grid(row=18, column=6)
        saved_pen = Entry(self.third_frame, width=5, font=self.myFont2)
        saved_pen.grid(row=19, column=6)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=15, column=3)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=15, column=5)

        win_var = IntVar()
        win = Checkbutton(self.third_frame, text="Win", font=self.myFont2, variable=win_var, onvalue=1,
                          offvalue=0)
        win.grid(row=18, column=2)

        lost_var = IntVar()
        lost = Checkbutton(self.third_frame, text="Lost", font=self.myFont2, variable=lost_var, onvalue=1,
                           offvalue=0)
        lost.grid(row=19, column=2)

        Label(self.third_frame, text="\n").grid(row=17, column=1)

        Label(self.third_frame,
              text="                                                    ").grid(
            row=18, column=1)

        starter_var = IntVar()
        starter = Checkbutton(self.third_frame, text="Starter", font=self.myFont2, variable=starter_var, onvalue=1,
                              offvalue=0, anchor=E)
        starter.grid(row=20, column=0)

        Label(self.third_frame,
              text="\n" + "\n" + "\n" + "\n").grid(
            row=20, column=1)

        def call_compute_rating_gk():
            try:
                self.compute_rating(int(goals.get()),
                                    int(assists.get()), int(shotsont.get()),
                                    int(dribblings.get()), int(keypasses.get()),
                                    int(touches.get()), int(passes_acc.get()),
                                    int(crosses_acc.get()), int(lballs_acc.get()),
                                    int(grduels_w.get()),
                                    int(aerials_w.get()), int(poss_lost.get()),
                                    int(clearances.get()), int(stop_shots.get()),
                                    int(interceptions.get()),
                                    int(tackles.get()), varyellow.get(), var.get(),
                                    int(owngoals.get()),
                                    int(actions_involved.get()), int(actions_total.get()), int(actions_shot.get()),
                                    win_var.get(),
                                    lost_var.get(),
                                    starter_var.get(), choice, role,
                                    cal_mov.get_date(), int(goals_ag_otb.get()), int(goals_ag_itb.get()),
                                    int(saves_itb.get()), int(saves_otb.get()), int(saved_pen.get()), 1)
                print("ok")
            except:
                messagebox.showerror("Error","Please, make sure you have entered all fields correctly")

        Button(self.third_frame, text="Compute the rating", font=self.myFont3, padx=25, pady=5, bg="#3bab5a",
               fg="white", command=call_compute_rating_gk).grid(row=22, column=3)



        self.frame_mov.grid_forget()
        self.frame_gk.grid(row=3, column=1)
        self.frame_gk.tkraise()




    def display_mov(self, choice, role):

        self.frame_mov.forget()

        Label(self.second_frame, text="Goals", font=self.myFont2).grid(row=0, column=2)
        goals = Entry(self.second_frame, width=5, font=self.myFont2)
        goals.grid(row=1, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=1, column=1)

        Label(self.second_frame, text="Assists", font=self.myFont2).grid(row=0, column=4)
        assists = Entry(self.second_frame, width=5, font=self.myFont2)
        assists.grid(row=1, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=1, column=3)

        Label(self.second_frame, text="Shots on target", font=self.myFont2).grid(row=12, column=0)
        shotsont = Entry(self.second_frame, width=5, font=self.myFont2)
        shotsont.grid(row=13, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=1, column=5)

        Label(self.second_frame, text="Key passes", font=self.myFont2).grid(row=0, column=6)
        keypasses = Entry(self.second_frame, width=5, font=self.myFont2)
        keypasses.grid(row=1, column=6)

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

        Label(self.second_frame, text="Accurated crosses", font=self.myFont2).grid(row=3, column=6)
        crosses_acc = Entry(self.second_frame, width=5, font=self.myFont2)
        crosses_acc.grid(row=4, column=6)

        Label(self.second_frame, text="\n").grid(row=5, column=1)

        Label(self.second_frame, text="Accurated long passes", font=self.myFont2).grid(row=6, column=0)
        lballs_acc = Entry(self.second_frame, width=5, font=self.myFont2)
        lballs_acc.grid(row=7, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=7, column=1)

        Label(self.second_frame, text="Stopped shots", font=self.myFont2).grid(row=6, column=2)
        stop_shots = Entry(self.second_frame, width=5, font=self.myFont2)
        stop_shots.grid(row=7, column=2)

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
        rcards.grid(row=15, column=0)

        varyellow = IntVar()
        ycards = Checkbutton(self.second_frame, text="Yellow Cards", font=self.myFont2, variable=varyellow, onvalue=1,
                             offvalue=0)
        ycards.grid(row=16, column=0)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=12, column=1)

        Label(self.second_frame, text="Own goals", font=self.myFont2).grid(row=12, column=2)
        owngoals = Entry(self.second_frame, width=5, font=self.myFont2)
        owngoals.grid(row=13, column=2)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=12, column=3)



        Label(self.second_frame,
              text="                                                    ").grid(
            row=12, column=5)



        Label(self.second_frame, text="\n").grid(row=14, column=1)

        Label(self.second_frame, text="# actions in which" + "\n" + "player is involved", font=self.myFont2).grid(row=12, column=4)
        actions_involved = Entry(self.second_frame, width=10, font=self.myFont2)
        actions_involved.grid(row=13, column=4)

        Label(self.second_frame, text="# actions which end with"+"\n"+"a shot where" + "\n" + "player is involved", font=self.myFont2).grid(
            row=15, column=4)
        actions_shot = Entry(self.second_frame, width=10, font=self.myFont2)
        actions_shot.grid(row=16, column=4)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=15, column=1)

        Label(self.second_frame, text="Select the date of the match").grid(row=0, column=0)
        cal_mov = DateEntry(self.second_frame, width=12, year=2022, month=4, day=11, background='darkblue',
                            foreground='white', borderwidth=2)
        cal_mov.grid(row=1, column=0)

        Label(self.second_frame, text="# total actions" + "\n" + "of team", font=self.myFont2).grid(row=12, column=6)
        total_actions = Entry(self.second_frame, width=10, font=self.myFont2)
        total_actions.grid(row=13, column=6)

        Label(self.second_frame,
              text="                                                    ").grid(
            row=15, column=3)


        Label(self.second_frame,
              text="                                                    ").grid(
            row=15, column=5)

        win_var = IntVar()
        win = Checkbutton(self.second_frame, text="Win", font=self.myFont2, variable=win_var, onvalue=1,
                          offvalue=0)
        win.grid(row=15, column=2)

        lost_var = IntVar()
        lost = Checkbutton(self.second_frame, text="Lost", font=self.myFont2, variable=lost_var, onvalue=1,
                           offvalue=0)
        lost.grid(row=16, column=2)

        Label(self.second_frame, text="\n").grid(row=17, column=1)


        Label(self.second_frame,
              text="                                                    ").grid(
            row=18, column=1)

        starter_var = IntVar()
        starter = Checkbutton(self.second_frame, text="Starter", font=self.myFont2, variable=starter_var, onvalue=1,
                           offvalue=0,anchor=E)
        starter.grid(row=17, column=2)


        Label(self.second_frame,
              text="\n" + "\n" + "\n" + "\n").grid(
            row=20, column=1)


        def call_compute_rating():
            try:
                self.compute_rating(int(goals.get()),
               int(assists.get()), int(shotsont.get()),int(dribblings.get()), int(keypasses.get()),
               int(touches.get()), int(passes_acc.get()), int(crosses_acc.get()), int(lballs_acc.get()), int(grduels_w.get()),
               int(aerials_w.get()), int(poss_lost.get()),
               int(clearances.get()), int(stop_shots.get()), int(interceptions.get()),
               int(tackles.get()), varyellow.get(), var.get(),  int(owngoals.get()),
               int(actions_involved.get()), int(total_actions.get()), int(actions_shot.get()), win_var.get(),
               lost_var.get(),
               starter_var.get(), choice, role, cal_mov.get_date(), 0,0,0,0,0,0)
            except:
                messagebox.showerror("Error","Please, make sure you have entered all fields correctly")

        Button(self.second_frame, text="Compute the rating", font=self.myFont3, padx=25, pady=5, bg="#3bab5a",
               fg="white", command= call_compute_rating).grid(row=20, column=3)





        self.frame_mov.grid(row=3, column=1)
        self.frame_mov.tkraise()

    def compute_rating(self, goals, assists, shotsont, dribblings, keypasses, touches, passes_acc, crosses_acc,
                       lballs_acc, grduels_w, aerials_w, poss_lost_w, clearances, stop_shots, interceptions, tackles,
                       ycards, rcards, owngoals, actions_involved, total_actions, actions_shot,
                       win, lost, starter, choice, role, date_mov, goals_ag_otb, goals_ag_itb, saves_itb, saves_otb, saved_pen, GK):

        flow_centrality = actions_involved/total_actions

        if(role == 'Goalkeeper'):
            flow_success = (actions_shot/total_actions) * 0.042
        elif(role == 'Defender'):
            flow_success = (actions_shot / total_actions) * 0.073
        elif(role == 'Midfielder'):
            flow_success = (actions_shot / total_actions) * 0.113
        else:
            flow_success = (actions_shot / total_actions) * 0.159

        input_data = [[goals, assists, shotsont, dribblings, keypasses, touches, passes_acc, crosses_acc,
                       lballs_acc, grduels_w, aerials_w, poss_lost_w, clearances, stop_shots, interceptions, tackles, ycards,
                       rcards,goals_ag_otb,goals_ag_itb,saves_itb,saves_otb,saved_pen, owngoals, flow_centrality, flow_success,
                       win, lost, starter, GK]]


        result = self.model.predict(input_data)
        #print(input_data)

        text_final = f"The rating is {int(result[0])}"

        messagebox.showinfo("Rating result", text_final)

        stmt5 = "INSERT INTO soccer_ratings.performance (`Username`, `Player`, `Date`, `rating`, `role`) VALUES (%s, %s, %s, %s, %s) "
        data_insert = [self.username, choice, date_mov, int(result[0]), role]
        db.mycursor.execute(stmt5,data_insert)










