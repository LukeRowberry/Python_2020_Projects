from tkinter import *
from tkinter import messagebox as mb
HEIGHT = 250
WIDTH = 250

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        error = Button(self, text="Error", command=self.onError)
        error.grid(padx=5, pady=5)

        warning = Button(self, text="Warning", command=self.onWarn)
        warning.grid(row=1, column=0)

        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)

        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)

    def onError(self):
        mb.showerror("Error", "Could not shower")

    def onWarn(self):
        mb.showwarning("Warning", "You probably should shower")

    def onQuest(self):
        result = mb.askquestion("Question", "Did you shower?")

        if result == "yes":
            print("You clicked yes")
        else:
            print("You clicked no")

    def onInfo(self):
        mb.showinfo("Info","It is good to shower often")



root = Tk()
root.title("Dialogue")
root.geometry(str(WIDTH)+"x"+str(+HEIGHT))
app = App(root)

root.mainloop()