import tkinter as tk
import sqlite3
from tkinter.constants import ACTIVE, DISABLED

from database import createAccount
    

LARGE_FONT= ("Verdana", 12)
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        import main as HOMEPAGE
        tk.Frame.__init__(self, parent)
        HEIGHT = 550 
        WIDTH = 350
       
        self.ErrorMsg = tk.Label(self, text = "",font=(None,10), fg='red')
        self.ErrorMsg.place(x = (WIDTH/2),y = 20)
        title = tk.Label(self, text = "Sign Up",font=(None,20),)
        title.place(x = (WIDTH/2+40),y = 40)
        user_nameLabel = tk.Label(self, text = "Create Username: ",font=(None,14))
        user_nameLabel.place(x = (WIDTH/2 + 18),y = 90)
        self.Username = tk.Entry(self)
        self.Username.place(x = (WIDTH/2 - 18),y = 120)
        passwordLabel = tk.Label(self, text = "Create Password: ",font=(None,14))
        passwordLabel.place(x = (WIDTH/2 + 18),y = 175)
        self.Password = tk.Entry(self,)
        self.Password.place(x = (WIDTH/2 - 18),y = 210)
        
       
        signUpBtn = tk.Button(self, text="Create Account", height = 3,
       
        width = 20, bg="red", command=self.signUp, highlightbackground="red" )
        signUpBtn.place(x = (WIDTH/2 - 18),y = 250)
        
      
        goBackBtn = tk.Button(self, text="Go back", height = 3, 
                width = 15, bg="red",  command=lambda: controller.show_frame(HOMEPAGE.StartPage), highlightbackground="lightblue")
        goBackBtn.place(x = (WIDTH/2 + 200),y = 270,)

    def signUp(self):
        #print("Hello?")
        print(f'Username: f{self.Username.get()} and Password: f{self.Password.get()}')

        conn = sqlite3.connect("data.db")
        c = conn.cursor()

        c.execute("""SELECT * FROM quiz_data""")
        data = c.fetchall()
        success = True
        
        for users in data:
            print("Hello?")

            if users[0].lower() == self.Username.get().lower():
                self.ErrorMsg.config(text="Username already exists. Try again!")
                success = False
        if success:
            createAccount(self.Username.get(),self.Password.get())

        