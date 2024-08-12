import tkinter as tk
from tkinter import ttk

my_text = "The Button is sad"

#create main window
root = tk.Tk()
root.title("My First GUI Programm")
root.minsize(width=500, height=300)
frm = ttk.Frame(root, padding=10)
frm.grid()

#button
button = ttk.Button(frm, text="Press", command=lambda: [button_click()]).grid(column=1, row=0)

#label
change = ttk.Label(frm, text=my_text)
change.grid(column=0, row=0)
frm.pack()

def button_click():
    print("i got clicked")
    change.config(text="The Button is happy")

#-----------------------------------------------------------------------------------------------------------
#fetch input
text = ttk.Label(frm, text="change me")
text.grid(column=0, row=1)

button2 = ttk.Button(frm, text="Change", command=lambda: [change_word()]).grid(column=3, row=1)

def change_word():
    text.config(text=input.get())
    pass

input = tk.Entry(frm, width=10)
input.grid(column=1, row=1)
answer = input.get()
print(answer)

#-----------------------------------------------------------------------------------------------------------





root.mainloop()

