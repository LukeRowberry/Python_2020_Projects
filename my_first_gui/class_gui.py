#Luke Rowberry
#1-20-2021
#Class Gui
from tkinter import *

class Application(Frame):
    """A gui app with three buttons"""

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
        self.clicks = 0
    def create_widgets(self):
        self.tclbl = Label(self,text = "Total Clicks")
        self.numclicks = Label(self,text = str(self.clicks))

        self.addbttn = Button(self,text = "+ to Clicks")
        self.minbttn = Button(self, text="- to Clicks")
        self.colorbttn = Button(self, text="Change Color")

        self.tclbl.grid()
        self.numclicks.grid()
        self.addbttn.grid()
        self.minbttn.grid()
        self.colorbttn.grid()

root = Tk()
root.title("Luke's Gui")
root.geometry("720x719")
root.resizable(0,0)
root.configure(bg = "#630436")
app = Application(root)


root.mainloop()
