import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
#user defined function to create userID and password
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 14, "bold")
custom_font_3 = ("Calibri", 11, "bold","underline")
def main_application():
    Pressure_drop_calculations = tk.Tk()
    Pressure_drop_calculations.geometry("1000x700+400+100")
    Pressure_drop_calculations.configure(background="snow")
    Pressure_drop_calculations.title("Application to calculate pressure drop due to varying cross section ......by ASK")
    #function for lable inside the application
    def label_inside_main_application (parameter):
          lable=ttk.Label(text=parameter, font=custom_font_1, background="snow")
          return lable
    def lable_For_heading (parameter):
          lable=ttk.Label(text=parameter, font=custom_font_2, background="snow", foreground="dark green")
          return lable
    def lable_special (parameter):
          lable=ttk.Label(text=parameter, font=custom_font_3, background="snow", foreground="red")
          return lable
    def label_inside_frame1 (parameter):
          lable=ttk.Label(frame_for_oilspecification,text=parameter, font=custom_font_1,background=frame_for_oilspecification.cget("bg"), foreground="red")
          return lable
    def spinbox_inside_label(num1):
        spinbox_inside_farame3=ttk.Spinbox(frame_for_oilspecification, from_=0, to=250,foreground="ghostwhite",background="blue",font=("calibre",10),width=10)
        return spinbox_inside_farame3 
    #frame inside applications
    frame_for_oilspecification = tk.Frame(Pressure_drop_calculations, highlightbackground="black", highlightthickness=1,background= "palegreen1",width=335, height=380)
    frame_for_oilspecification.place(x=640,y=300)
    #  Load the shibaura machine image using PIL
    image_path = os.path.join(os.path.dirname(__file__), 'Picture1.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((330, 220), Image.LANCZOS)  # Resize the image to 200x150 pixels
    photo = ImageTk.PhotoImage(Picture1)
    label_for_shibauralogo = tk.Label(Pressure_drop_calculations, image=photo)
    label_for_shibauralogo.image = photo  # Keep a reference to avoid garbage collection
    label_for_shibauralogo.place(x=640,y=50)
    lable_For_heading("CALCULATION FOR PRESSURE DROP ACROSS VARIOUS CROSS SECTIONS").place(x=240,y=10)
    lable_special("BERNOULLIS THEORY").place(x=50,y=50)
    label_inside_main_application("Bernoullis theory is based on the Law of conservation of energy,the sum of potential energy,\
    \nkinetic energy and Flow energy at any point inside the flow domain will be equal ").place(x=50,y=70)
    lable_special("ASSUMPTIONS").place(x=50,y=110)
    label_inside_main_application("1.Flow should be incompressible,\
    \n2.Energy is conserved,\n3.Steady flow \n4.Inviscous fluids (but real fluids has viscosity, need to include head losses)").place(x=60,y=130) 
    #lable inside frame 1
    label_for_oil_spec=tk.Label(frame_for_oilspecification,text="SPECIFICATION OF THE OIL",background=frame_for_oilspecification.cget("bg"),foreground="black", font=custom_font_3)
    label_for_oil_spec.place(x=70, y=10)
    label_inside_frame1("Oil Code           = Shell Tellus S2 MX 46").place(x=20, y=30)
    label_inside_frame1("API Group          = GroupII").place(x=20, y=50)
    label_inside_frame1("Base Oil           = Mineral based oil").place(x=20,y=70)
    label_inside_frame1("Density            = 846 kg/m\u00b3").place(x=20,y=90)
    label_inside_frame1("kinematic viscosity= 46 cSt\n @40 deg ").place(x=20,y=110)
    label_inside_frame1("kinematic viscosity= 6.9 cSt\n @100 deg ").place(x=20,y=150)
    label_inside_frame1("Viscosity index    = 105").place(x=20,y=190)
    label_inside_frame1("Flash point        = 230 deg").place(x=20,y=210)
    label_inside_frame1("Pour point         = -30 deg").place(x=20,y=230)
    label_inside_frame1("Specific gravity   =  ").place(x=20,y=250)




    
  
    Pressure_drop_calculations.mainloop()
main_application()














