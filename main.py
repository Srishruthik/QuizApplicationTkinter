# Multi-frame tkinter application v2.3
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        height = 550 
        width = 350
       

        title = tk.Label(app, text = "Shruthik's Quiz Application",font=(None,20),)
        title.place(x = (width/2 - 30),y = 40)
        user_nameLabel = tk.Label(app, text = "Enter Username: ",font=(None,14))
        user_nameLabel.place(x = (width/2 + 18),y = 90)
        Username = tk.Entry(app, text="User Name")
        Username.place(x = (width/2 - 18),y = 120)
        passwordLabel = tk.Label(app, text = "Enter Password: ",font=(None,14))
        passwordLabel.place(x = (width/2 + 18),y = 175)
        password = tk.Entry(app, text="Password")
        password.place(x = (width/2 - 18),y = 210)
        loginBtn = tk.Button(app, text="Log in", height = 3,
        width = 20, bg="red", command=None, highlightbackground="red" )
        loginBtn.place(x = (width/2 - 18),y = 250)


        signup = tk.Button(app, text="Sign up", height = 3, 
                width = 15, bg="red", command=lambda: app.switch_frame(SignUp), highlightbackground="lightblue")
        signup.place(x = (width/2 + 200),y = 270,)


  
        
        #tk.Button(self, text="Open page one",
                  #command=lambda: master.switch_frame(PageOne)).pack()
        #tk.Button(self, text="Open page two",
                  #command=lambda: master.switch_frame(PageTwo)).pack()

class SignUp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="This is page one").pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(fill="both",expand=True)
if __name__ == "__main__":
    app = SampleApp()
    app.title("Shruthik's Quiz Application")
    app.geometry("550x350")
    app.resizable(False, False)
    app.mainloop()