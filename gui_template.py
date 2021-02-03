#The basic layout of ever tkinter gui and can be used anywhere
from tkinter import *
HEIGHT = 250
WIDTH = 250

class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        pass


root = Tk()
root.title("Name")
root.geometry(str(WIDTH)+"x"+str(+HEIGHT))
app = App(root)

root.mainloop()