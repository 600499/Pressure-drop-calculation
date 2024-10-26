import tkinter as tk
from tkinter import messagebox
from Pressure_drop_calculations import main_application

# Declaration of the function for user ID and password
def login():
    #user_id = entry_user_id.get()
    #password = entry_password.get()
    #if user_id == "admin" and password == "123":
        #messagebox.showinfo("Login", "Login Successful!")
        Application.destroy()
        main_application()# Open the main application
    #else:
        #messagebox.showerror("Login", "Invalid User ID or Password")
def label_inside_application (parameter):
    label_inside = tk.Label(Application,text=parameter,bg=Application.cget("bg"),font=custom_font1)
    return label_inside
custom_font1=("Calibri", 11, "bold")
# Creating the main window
Application = tk.Tk()
Application.title("Login Application ......by ASK")
Application.config(bg="grey70")
Application.geometry("370x200")
# Creating the label
label_inside_application("User ID:").place(x=50, y=20)
label_inside_application("(Enter the user ID)").place(x=155, y=40)
label_inside_application("(Enter the user Password)").place(x=130, y=90)
label_inside_application("Password:").place(x=50, y=70)
# Creating for entry for user Id and password
entry_user_id = tk.Entry(Application, background="oliveDrab3")
entry_user_id.place(x=150, y=20)
entry_password = tk.Entry(Application, show="*", background="oliveDrab3")  # `show="*"` hides the password input
entry_password.place(x=150, y=70)
# Creating the Login button
button_login = tk.Button(Application, text="Login", command=login, width=10)
button_login.place(x=170, y=130)
# Running the application
Application.mainloop()