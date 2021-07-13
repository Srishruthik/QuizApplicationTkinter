from tkinter import *
import tkinter.font as tkFont
app = Tk()
app.title("Shruthik's Quiz Application")
app.geometry("550x350")
height = 550 
width = 350

title = Label(app, text = "Shruthik's Quiz Application",font=(None,20)).place(x = (width/2 - 30),y = 40)
user_nameLabel = Label(app, text = "Enter Username: ",font=(None,14)).place(x = (width/2 + 18),y = 90)
Username = Entry(app, text="User Name").place(x = (width/2 - 18),y = 120)


passwordLabel = Label(app, text = "Enter Password: ",font=(None,14)).place(x = (width/2 + 18),y = 175)



app.resizable(False, False)
app.mainloop()
