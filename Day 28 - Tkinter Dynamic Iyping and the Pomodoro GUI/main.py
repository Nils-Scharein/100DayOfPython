import tkinter as tk
import time


WIDTH = 600
HEIGHT = 600


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- UI SETUP ------------------------------- #
#main Frame
root = tk.Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

# ---------------------------- Pomodoro Clas ------------------------------- #

class Pomodoro(tk.Tk):
    def __init__(self, root):

        self.STOP = False
        self.timer = 0
        self.work = 1500
        self.shortbreak = 300
        self.longbreak = 1800

        #get Img + create Canvas
        self.tomato_img = tk.PhotoImage(file="tomato.png")

        self.canvas = tk.Canvas(root, width=200, height=224, bg=YELLOW,
                           highlightthickness=0)  # Set canvas size to match window size
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.canvas.grid(column=1, row=1)

        #Timer, Work, Break Lael
        self.timer_label = tk.Label(root, text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
        self.timer_label.grid(column=1, row=0)

        #countdown in tomato
        self.timer_countdowm = self.canvas.create_text(103, 130, text="00:00", fill="White", font=(FONT_NAME, 30, "bold"))

        #Checks
        self.checks = tk.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
        self.checks.grid(column=1, row=4)

        #Start
        self.startButton = tk.Button(text="Start", command=self.mechanism)
        self.startButton.grid(column=0, row=3)

        #Reset
        self.resetButton = tk.Button(text="Reset", command=self.reset)
        self.resetButton.grid(column=2, row=3)

        #Work,short break, longbreak
        self.work_label = tk.Label(text="Work Time", bg=YELLOW)
        self.work_label.grid(column=0, row=5)
        self.work_input = tk.Entry(bg=YELLOW)
        self.work_input.grid(column=1, row=5)
        self.shortbreak_label = tk.Label(text="Short Break Time", bg=YELLOW)
        self.shortbreak_label.grid(column=0, row=6)
        self.shortbreak_input = tk.Entry(bg=YELLOW)
        self.shortbreak_input.grid(column=1, row=6)
        self.longbreak_label = tk.Label(text="Long Break Time", bg=YELLOW)
        self.longbreak_label.grid(column=0, row=7)
        self.longbreak_input = tk.Entry(bg=YELLOW)
        self.longbreak_input.grid(column=1, row=7)

    def countdown(self, status, t):
        while t > -1 and self.STOP == False:
            mins, secs = divmod(t, 60)
            self.timer = '{:02d}:{:02d}'.format(mins, secs)
            self.canvas.itemconfig(self.timer_countdowm, text=self.timer)
            self.timer_label.config(text=status)
            root.update()
            root.after(1000)
            if t == 1:
                root.lift()
                root.attributes('-topmost', True)
                root.after_idle(root.attributes, '-topmost', False)
            t -= 1

    def update_checks(self, number_of_times):
        if self.STOP == True:
            pass
        else:
            self.checks.config(text=str(number_of_times * u"\u2713"))

    def mechanism(self):
        self.checks.config(text="")

        if self.work_input.get().isdigit() and self.work_input.get() != "":
            self.work = int(self.work_input.get())*60
        if self.shortbreak_input.get().isdigit() and self.shortbreak_input.get() != "":
            self.shortbreak = int(self.shortbreak_input.get())*60
        if self.longbreak_input.get().isdigit() and self.longbreak_input.get() != "":
            self.longbreak = int(self.longbreak_input.get())*60

        self.STOP = False
        self.countdown("Work", self.work)
        self.update_checks(1)
        self.countdown("Break", 3)
        self.countdown("Work", self.work)
        self.update_checks(2)
        self.countdown("Break", 3)
        self.countdown("Work", self.work)
        self.update_checks(3)
        self.countdown("Long Break", self.longbreak)

    def reset(self):
        self.STOP = True
        self.work = 1500
        self. shortbreak = 300
        self. longbreak = 1800
        self.checks.config(text="")
        self.timer_label.config(text="Timer")
        self.canvas.itemconfig(self.timer_countdowm, text='{:02d}:{:02d}'.format(0, 0))

pomodoro = Pomodoro(root)

root.mainloop()