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
    def label_inside_inputframe (parameter):
          lable=ttk.Label(frame_for_inputparameters,text=parameter, font=custom_font_1,background=frame_for_oilspecification.cget("bg"), foreground="red")
          return lable
    def label_inside_hintframe (parameter):
          lable=ttk.Label(frame_for_hints,text=parameter, font=custom_font_1,background=frame_for_oilspecification.cget("bg"), foreground="red")
          return lable
    def spinbox_inside_label(num1):
        spinbox_inside_farame3=ttk.Spinbox(frame_for_oilspecification, from_=0, to=250,foreground="ghostwhite",background="blue",font=("calibre",10),width=10)
        return spinbox_inside_farame3
    spinboxes = {}
    def spinbox_inside_resultframe(Name):
      spinbox_inside_resultframe=tk.Spinbox(frame_for_result, from_=0, to=250, background="white", foreground="white",font=("calibre",10),width=10)
      spinboxes[Name]=spinbox_inside_resultframe
      return spinbox_inside_resultframe 
    def label_inside_resultframe (parameter):
          lable=ttk.Label(frame_for_result,text=parameter, font=custom_font_1,background=frame_for_oilspecification.cget("bg"), foreground="black")
          return lable
    #frame inside applications
    frame_for_oilspecification = tk.Frame(Pressure_drop_calculations, highlightbackground="black", highlightthickness=1,background= "palegreen1",width=335, height=280)
    frame_for_oilspecification.place(x=640,y=270)
    frame_for_inputparameters = tk.Frame(Pressure_drop_calculations, highlightbackground="black", highlightthickness=1,background= "palegreen1",width=580, height=150)
    frame_for_inputparameters.place(x=50,y=270)
    frame_for_hints = tk.Frame(Pressure_drop_calculations, highlightbackground="black", highlightthickness=1,background= "palegreen1",width=335, height=130)
    frame_for_hints.place(x=640,y=560)
    frame_for_result = tk.Frame(Pressure_drop_calculations, highlightbackground="black", highlightthickness=1,background= "palegreen1",width=580, height=235)
    frame_for_result.place(x=50,y=455)
    #  Load the shibaura machine image using PIL
    image_path = os.path.join(os.path.dirname(__file__), 'Picture1.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((330, 220), Image.LANCZOS)  # Resize the image to 200x150 pixels
    photo = ImageTk.PhotoImage(Picture1)
    label_for_cross_section = tk.Label(Pressure_drop_calculations, image=photo)
    label_for_cross_section.image = photo  # Keep a reference to avoid garbage collection
    label_for_cross_section.place(x=640,y=40)
    image_path2 = os.path.join(os.path.dirname(__file__), 'Picture2.png')
    Picture2 = Image.open(image_path2)
    Picture2 = Picture2.resize((200, 120), Image.LANCZOS)  # Resize the image to 200x150 pixels
    photo = ImageTk.PhotoImage(Picture2)
    label_for_equation = tk.Label(frame_for_inputparameters, image=photo)
    label_for_equation.image = photo  # Keep a reference to avoid garbage collection
    label_for_equation.place(x=350,y=10)
    image_path3 = os.path.join(os.path.dirname(__file__), 'Picture4.png')
    Picture3 = Image.open(image_path3)
    Picture3 = Picture3.resize((50,50), Image.LANCZOS)  # Resize the image to 200x150 pixels
    photo = ImageTk.PhotoImage(Picture3)
    label_for_thumb = tk.Label(frame_for_hints, image=photo)
    label_for_thumb.image = photo  # Keep a reference to avoid garbage collection
    label_for_thumb.place(x=220,y=5)

    lable_For_heading("CALCULATION FOR PRESSURE DROP ACROSS VARIOUS CROSS SECTIONS").place(x=240,y=10)
    lable_special("BERNOULLIS THEORY").place(x=50,y=50)
    label_inside_main_application("Bernoullis theory is based on the Law of conservation of energy,the sum of potential energy,\
    \nkinetic energy and Flow energy at any point inside the flow domain will be equal. ").place(x=50,y=70)
    lable_special("ASSUMPTIONS").place(x=50,y=110)
    label_inside_main_application("1.Flow should be incompressible,\
    \n2.Energy is conserved,\n3.Steady flow, \n4.Inviscous fluids (but real fluids has viscosity, need to include head losses)").place(x=60,y=130) 
    #lable inside frame 1
    label_for_oil_spec=tk.Label(frame_for_oilspecification,text="SPECIFICATION OF THE OIL",background=frame_for_oilspecification.cget("bg"),foreground="black", font=custom_font_3)
    label_for_oil_spec.place(x=70, y=10)
    label_for_hints=tk.Label(frame_for_hints,text="HINTS",background=frame_for_oilspecification.cget("bg"),foreground="black", font=custom_font_3)
    label_for_hints.place(x=140, y=10)
    label_for_Calculation_result=tk.Label(Pressure_drop_calculations,text="CALCULATION RESULTS",background=Pressure_drop_calculations.cget("bg"),foreground="black", font=custom_font_3)
    label_for_Calculation_result.place(x=250, y=425)

    label_inside_frame1("Oil Code                      = Shell Tellus S2 MX 46").place(x=20, y=30)
    label_inside_frame1("API Group                   = GroupII").place(x=20, y=50)
    label_inside_frame1("Base Oil                       = Mineral based oil").place(x=20,y=70)
    label_inside_frame1("Density                        = 846 kg/m\u00b3").place(x=20,y=90)
    label_inside_frame1("kinematic viscosity = 46 cSt\n @40 deg ").place(x=20,y=110)
    label_inside_frame1("kinematic viscosity = 6.9 cSt\n @100 deg ").place(x=20,y=150)
    label_inside_frame1("Viscosity index         = 105").place(x=20,y=190)
    label_inside_frame1("Flash point                 = 230 deg").place(x=20,y=210)
    label_inside_frame1("Pour point                  = -30 deg").place(x=20,y=230)
    label_inside_frame1("Specific gravity         = 0.846  ").place(x=20,y=250)
    inlet_port_size = [ "G-1/8", "G-1/4", "G-3/4", "G-3/8", "G-1", "G-1 1/4", "G-1 1/2" ]
    combobox_for_inletPort_size = ttk.Combobox(frame_for_inputparameters, values=inlet_port_size,width=11)
    combobox_for_inletPort_size.place(x=120, y=30)
    combobox_for_outletPort_size = ttk.Combobox(frame_for_inputparameters, values=inlet_port_size,width=11)
    combobox_for_outletPort_size.place(x=120, y=70)
    power_pack = [ "11", "22", "30", "37", "45", "55", "75", "90", "110", "135" ]
    combobox_for_inletPort_size = ttk.Combobox(frame_for_inputparameters, values=power_pack,width=11)
    combobox_for_inletPort_size.place(x=120, y=110)
    spinbox_inside_resultframe("spinbox_for_inlet_area").place(x=50, y=35)
    spinbox_inside_resultframe("spinbox_for_outlet_area").place(x=50, y=85)
    spinbox_inside_resultframe("spinbox_for_arearatio").place(x=50, y=135)
    spinbox_inside_resultframe("spinbox_for_flowrate").place(x=50, y=185)
    spinbox_inside_resultframe("spinbox_for_inletvelocity").place(x=250, y=35)
    spinbox_inside_resultframe("spinbox_for_outletvelocity").place(x=250, y=85)
    spinbox_inside_resultframe("spinbox_for_pressuredrop").place(x=250, y=135)


    label_inside_inputframe("Select the inlet port size [mm or inch]").place(x=50, y=10)
    label_inside_inputframe("Select the outlet port size [mm or inch]").place(x=50, y=50)
    label_inside_inputframe("Select the Powerpack [kW]").place(x=50, y=90)
    label_inside_resultframe("Inlet Area [mm\u00b2]").place(x=50, y=10)
    label_inside_resultframe("Outlet Area [mm\u00b2]").place(x=50, y=60)
    label_inside_resultframe("Area ratio").place(x=50, y=110)
    label_inside_resultframe("Flow rate [LPM]").place(x=50, y=160)
    label_inside_resultframe("Inlet velocity [m/s]").place(x=250, y=10)
    label_inside_resultframe("Outlet velocity [m/s]").place(x=250, y=60)
    label_inside_resultframe("Pressure drop [bar]").place(x=250, y=110)


    label_inside_hintframe("1 st = 10\u2074 m\u00b2/sec").place(x=50, y=30)
    label_inside_hintframe("1 ct = 10\u2076 m\u00b2/sec").place(x=50, y=50)
    label_inside_hintframe("1 pascal = 10\u2075 bar").place(x=50, y=70)
    label_inside_hintframe("1 Mega pascal = 10 bar").place(x=50, y=90)







    
  
    Pressure_drop_calculations.mainloop()
main_application()














