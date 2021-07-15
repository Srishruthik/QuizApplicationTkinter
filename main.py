
import tkinter as tk
from signup import PageOne
from database import signInAccount
LARGE_FONT= ("Verdana", 12)
from menu import menuScreen

import sqlite3
class QuizApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, menuScreen):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        HEIGHT = 550 
        WIDTH = 350
        self.ErrorMsg = tk.Label(self, text = "",font=(None,10), fg='red')
        self.ErrorMsg.place(x = (WIDTH/2),y = 20)

        title = tk.Label(self, text = "Shruthik's Quiz Application",font=(None,20),)
        title.place(x = (WIDTH/2 - 30),y = 40)
        user_nameLabel = tk.Label(self, text = "Enter Username: ",font=(None,14))
        user_nameLabel.place(x = (WIDTH/2 + 18),y = 90)
        self.Username = tk.Entry(self, text="User Name")
        self.Username.place(x = (WIDTH/2 - 18),y = 120)
        passwordLabel = tk.Label(self, text = "Enter Password: ",font=(None,14))
        passwordLabel.place(x = (WIDTH/2 + 18),y = 175)
        self.Password = tk.Entry(self, text="Password")
        self.Password.place(x = (WIDTH/2 - 18),y = 210)
        loginBtn = tk.Button(self, text="Log in", height = 3,
        width = 20, bg="red", command=self.signIn, highlightbackground="red" )
        loginBtn.place(x = (WIDTH/2 - 18),y = 250)


        signup = tk.Button(self, text="Sign Up", height = 3, 
                width = 15, bg="red",  command=lambda: controller.show_frame(PageOne), highlightbackground="lightblue")
        signup.place(x = (WIDTH/2 + 200),y = 270,)



    def signIn(self):
        #lambda: controller.show_frame(menuScreen)
        print(f'Username: f{self.Username.get()} and Password: f{self.Password.get()}')

        conn = sqlite3.connect("data.db")
        c = conn.cursor()

        c.execute("""SELECT * FROM quiz_data""")
        data = c.fetchall()
        success = False
        
        for users in data:

            if users[0].lower() == self.Username.get().lower() and users[1].lower() == self.Password.get().lower():
                signInAccount(self.Username.get(),self.Password.get())
                success = True
                self.controller.show_frame(menuScreen)
                self.ErrorMsg.config(text="Logging in... ",fg="green")
                
                break
        if not success:
            self.ErrorMsg.config(text="Incorrect Username or Password")





app = QuizApp()
app.title("Shruthik's Quiz Application")
app.geometry("550x350")
app.resizable(False, False)
app.mainloop()