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
        self.lbl = Label(self,text = "Enter your username and password to gain entry")
        self.lbl.grid(row =0,column =0,columnspan =3,sticky = N)

        self.lbl_user = Label(self, text="Username:")
        self.lbl_user.grid(row=1, sticky=W)

        self.lbl_pass = Label(self, text="Password:")
        self.lbl_pass.grid(row=2, sticky=W)

        self.bttn = Button(self,text = "Login")
        self.bttn.grid(row=3,sticky = E)
        self.bttn["command"] = self.submit

        self.text_user = Entry(self)
        self.text_user.grid(row=1, column=1,columnspan=2,sticky = W)

        self.text_pass = Entry(self,show = "*")
        self.text_pass.grid(row=2, column=1, columnspan=2,sticky = W)

        self.output = Text(self)
        self.output.grid(row = 4,columnspan = 3)

        self.new = Button(self,text = "New User")
        self.new.grid(row = 3,column =1,sticky = W)
        self.new["command"] = self.create_new_user

    def submit(self):
        username = self.text_user.get()
        password = self.text_pass.get()
        if username.lower() in self.usernames:
            user_index = self.usernames.index(username)
            if password in self.passwords[user_index]:
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

    def create_new_user(self):
        self.lbl.config(text = "Enter a username and password to create a new account")
        self.lbl_user.config(text = "New Username")
        self.lbl_pass.config(text = "New Password")
        self.text_user.delete(0,END)
        self.text_pass.delete(0,END)
        self.bttn.grid_remove()
        self.bttn2 = Button(self,text = "Create")
        self.bttn2.grid(row=3,sticky = E)
        self.bttn2["command"] = self.create
        
    def create(self):
        username = self.text_user.get()
        password = self.text_pass.get()
        
        if username.lower() in self.usernames:
                message = "User already exits"
                self.output.delete(0.0,END)
                self.output.insert(0.0,message)
        else:
            self.usernames.append(username)
            self.passwords.append(password)
            message = "Success - Login to grant access"
            self.output.delete(0.0,END)
            self.output.insert(0.0,message)
                

        self.lbl.config(text = "Enter your username and password to gain entry")
        self.lbl_user.config(text = "Username:")
        self.lbl_pass.config(text = "Password:")
        self.bttn2.grid_remove()
        self.bttn.grid()
        self.text_user.delete(0,END)
        self.text_pass.delete(0,END)
        self.tries = 0
        
        
def main():
    root = Tk()
    root.title("Password Entry")
    root.geometry("650x500")
    app = App(root)
    root.mainloop()
main()
