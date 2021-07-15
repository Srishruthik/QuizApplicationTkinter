import tkinter as tk
from database import signInAccount
class menuScreen(tk.Frame):

    def __init__(self, parent, controller):
        import main as HOMEPAGE
        tk.Frame.__init__(self, parent)
        HEIGHT = 550 
        WIDTH = 350
       
      
        title = tk.Label(self, text = "Hello World",font=(None,20),)
        title.place(x = (WIDTH/2+40),y = 40)
        
       
      
        goBackBtn = tk.Button(self, text="Go back", height = 3, 
                width = 15, bg="red",  command=lambda: controller.show_frame(HOMEPAGE.StartPage), highlightbackground="lightblue")
        goBackBtn.place(x = (WIDTH/2 + 200),y = 270,)