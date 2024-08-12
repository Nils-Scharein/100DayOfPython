import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

#Miles
miles_label = ttk.Label(root, text="Miles").grid(column=2, row=0)
miles_input = ttk.Entry(validate="all", validatecommand="%P")
miles_input.grid(column=1, row=0)

#KM
km_text = ttk.Label(root, text="is equal to").grid(column=0, row=1)
km_umgerechnet = ttk.Label(root, text=0)
km_umgerechnet.grid(column=1, row=1)
km_unit = ttk.Label(root, text="Km").grid(column=2, row=1)

#Button umrechnung
def umrechnung():
    text = int(miles_input.get())
    if text == 0:
        km = 0
        km_umgerechnet.config(text=km)
    elif text == "":
        pass
    else:
        km = text * 1.60934
        km_umgerechnet.config(text=km)

button = ttk.Button(root, text="Press", command=umrechnung).grid(column=1, row=2)

root.mainloop()