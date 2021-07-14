
import tkinter as tk


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        height = 550 
        width = 350
       

        title = tk.Label(self, text = "Shruthik's Quiz Application",font=(None,20),)
        title.place(x = (width/2 - 30),y = 40)
        user_nameLabel = tk.Label(self, text = "Enter Username: ",font=(None,14))
        user_nameLabel.place(x = (width/2 + 18),y = 90)
        Username = tk.Entry(self, text="User Name")
        Username.place(x = (width/2 - 18),y = 120)
        passwordLabel = tk.Label(self, text = "Enter Password: ",font=(None,14))
        passwordLabel.place(x = (width/2 + 18),y = 175)
        password = tk.Entry(self, text="Password")
        password.place(x = (width/2 - 18),y = 210)
        loginBtn = tk.Button(self, text="Log in", height = 3,
        width = 20, bg="red", command=None, highlightbackground="red" )
        loginBtn.place(x = (width/2 - 18),y = 250)


        signup = tk.Button(self, text="Sign up", height = 3, 
                width = 15, bg="red",  command=lambda: controller.show_frame(PageOne), highlightbackground="lightblue")
        signup.place(x = (width/2 + 200),y = 270,)




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.title("Shruthik's Quiz Application")
app.geometry("550x350")
app.resizable(False, False)
app.mainloop()