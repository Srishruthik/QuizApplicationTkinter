from tkinter import *
import tkinter.font as tkFont
app = Tk()
app.title("Shruthik's Quiz Application")
app.geometry("550x350")
height = 550 
width = 350

title = Label(app, text = "Shruthik's Quiz Application",font=(None,20)).place(x = (width/2 - 30),y = 40)


user_nameLabel = Label(app, text = "Enter Username: ",font=(None,14))
user_nameLabel.place(x = (width/2 + 18),y = 90)

Username = Entry(app, text="User Name")
Username.place(x = (width/2 - 18),y = 120)


passwordLabel = Label(app, text = "Enter Password: ",font=(None,14))
passwordLabel.place(x = (width/2 + 18),y = 175)

password = Entry(app, text="Password")
password.place(x = (width/2 - 18),y = 210)

loginBtn = Button(app, text="Log in", height = 3, 
          width = 20, bg="blue")
loginBtn.place(x = (width/2 - 18),y = 250)







app.resizable(False, False)
app.mainloop()
