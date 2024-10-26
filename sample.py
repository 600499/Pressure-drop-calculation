from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x300")

def label_inside_frame1(text):
    # Use Calibri font with left alignment and padding for spacing
    return ttk.Label(root, text=text, font=("Calibri", 10), anchor="w", justify="left", padding=(0, 5))

# Align the equal signs by adding extra spaces manually for better visual alignment.
label_inside_frame1("Oil Code              = Shell Tellus S2 MX 46").place(x=20, y=30)
label_inside_frame1("API Group             = GroupII").place(x=20, y=50)
label_inside_frame1("Base Oil              = Mineral based oil").place(x=20, y=70)
label_inside_frame1("Density               = 846 kg/m\u00b3").place(x=20, y=90)
label_inside_frame1("kinematic viscosity   = 46 cSt\n @40 deg ").place(x=20, y=110)
label_inside_frame1("kinematic viscosity   = 6.9 cSt\n @100 deg ").place(x=20, y=150)
label_inside_frame1("Viscosity index       = 105").place(x=20, y=190)
label_inside_frame1("Flash point           = 230 deg").place(x=20, y=210)
label_inside_frame1("Pour point            = -30 deg").place(x=20, y=230)
label_inside_frame1("Specific gravity      = ").place(x=20, y=250)

root.mainloop()
