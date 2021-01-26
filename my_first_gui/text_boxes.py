#Shows text and entry widgets and the grid layout manager
from tkinter import *

class App(Frame):
    usernames = ["luke"]
    passwords = ["password"]
    tries = 0

    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self,text = "Enter your password to gain entry")
        self.lbl.grid(row =0,column =0,columnspan =3,sticky = N)

        self.lbl_user = Label(self, text="Username:")
        self.lbl_user.grid(row=1, sticky=W)

        self.lbl_pass = Label(self, text="Password:")
        self.lbl_pass.grid(row=2, sticky=W)

        self.bttn = Button(self,text = "Submit")
        self.bttn.grid(row=3)
        self.bttn["command"] = self.submit

        self.text_user = Entry(self)
        self.text_user.grid(row=1, column=1,columnspan=2)

        self.text_pass = Entry(self)
        self.text_pass.grid(row=2, column=1, columnspan=2)

        self.output = Text(self)
        self.output.grid(row = 4,columnspan = 3)

        self.new = Button(self,text = "New User")
        self.new.grid(row = 3,column =1)
        self.new["command"] = self.new_user

    def submit(self):
        username = self.text_user.get()
        password = self.text_pass.get()
        if username.lower() in self.usernames:
            if password in self.passwords:
                message = "Access Granted"
                self.tries = 0
            else:
                message = "Password Incorrect"
                self.tries += 1
        else:
            message = "Username Incorrect"
            self.tries += 1
        if self.tries > 3:
            message = "Contacting Authorities"
        self.output.delete(0.0,END)
        self.output.insert(0.0,message)

    def new_user(self):
        self.lbl_user = Label(self,text = "New Username")
        self.lbl_pass = Label(self,text = "New Password")
        #doesnt work








def main():
    root = Tk()
    root.title("Password Entry")
    root.geometry("750x600")
    app = App(root)
    root.mainloop()
main()