from tkinter import *
import tkinter.font as font

from Rating import Rating


class Panel:

    def __init__(self, root, frame):

        self.root = root
        self.frame = frame

        self.frame_rating = LabelFrame(self.root, pady=5, padx=5)

        myFont = font.Font(family='Calibri', size=14)
        myFont2 = font.Font(family='Calibri', size=12)
        label_insert_p = Label(frame, text="Insert a new player to the team",font=myFont)
        entry_insert_p = Entry(frame, width=25, font=myFont2)
        button_insert_p = Button(frame, text="Insert", padx=25, pady=5, bg="#3bab5a", fg="white",font=myFont2)
        space_label1 = Label(frame, text=" ")
        space_label2 = Label(frame, text=" ")
        space_label3 = Label(frame, text="\n"+"\n")

        label_insert_p.grid(row=2, column=1,columnspan=2)
        space_label1.grid(row=3,column=1)
        entry_insert_p.grid(row=4,column=1)
        space_label2.grid(row=5,column=1)
        button_insert_p.grid(row=4,column=2)
        space_label3.grid(row=7, column=1)

        rating_button = Button(frame, text="Rate a player",padx=25, pady=10, bg="#1d434e", fg="white",font=myFont2, command=self.open_rating)
        rating_button.grid(row=8, column=1)
        space_label4 = Label(frame, text="\n" + "\n")
        space_label4.grid(row=9,column=1)

        lineup_button = Button(frame, text="View the starting lineup", padx=25, pady=10, bg="#1d434e", fg="white",font=myFont2)
        lineup_button.grid(row=10, column=1)
        space_label5 = Label(frame, text="\n" + "\n")
        space_label5.grid(row=11, column=1)


        trend_button = Button(frame, text="View a player's performance trend", padx=25, pady=10, bg="#1d434e", fg="white",font=myFont2,command= self.indietro)
        trend_button.grid(row=12, column=1)

    def indietro(self):
        self.frame.grid_forget()

    def open_rating(self):
        Rating(self.root, self.frame_rating)
        self.frame_rating.grid(row=2, column=1)











