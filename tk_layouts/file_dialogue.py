#The basic layout of ever tkinter gui and can be used anywhere
from tkinter import *
from tkinter import filedialog
TITLE = "File Dialogue"
HEIGHT = 250
WIDTH = 250

class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open",command=self.onOpen)
        menubar.add_cascade(label="File",menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH,expand=1)

    def onOpen(self):
        ftypes = [("Python file", "*.py"), ("All files", "*")]
        dlg = filedialog.Open(self, filetypes=ftypes)
        f1=dlg.show()
        if f1 != "":
            text=self.readFile(f1)
            self.txt.insert(END,text)
    def readFile(self,filename):
        with open(filename,"r") as f:
            text = f.read()
        return text




root = Tk()
root.title(TITLE)
root.geometry(str(WIDTH)+"x"+str(+HEIGHT))
app = App(root)

root.mainloop()