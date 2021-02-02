#Luke Rowberry
#1-22-2021
#Click Counter Program
from tkinter import *


class App(Frame):
    """GUI appication which counts button clicks"""
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.total = 0
        self.colors = ["red","orange","yellow","green","blue","purple"]
        self.color_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl1 = Label(self,text = "Total People: ")
        self.lbl2 = Label(self,text = str(self.total))
        self.lbl3 = Label(self,text = "Activity: Low ",fg = "red")
        self.bttn_add = Button(self,text = "+ Person",width = 18, height = 1)
        self.bttn_add.config(command = self.add_to_count) #command
        self.bttn_min = Button(self,text = "- Person",width = 18, height = 1)
        self.bttn_min["command"] = self.min_to_count #command
        self.bttn_color = Button(self,text = "Change Color", command = self.change_color, width = 28, height = 3) #command

        self.bttn_color.grid()
        self.lbl1.grid()
        self.lbl2.grid()
        self.lbl3.grid()
        self.bttn_add.grid()
        self.bttn_min.grid()
        
    def add_to_count(self):
        self.total += 1
        self.lbl2.config(text = str(self.total))
        self.activity()
        
    def min_to_count(self):
        if self.total <= 0:
            self.total = 1
        self.total -= 1
        self.lbl2.config(text = str(self.total))
        self.activity()
        
    def change_color(self):
        self.config(bg = self.colors[self.color_index])
        self.lbl1.config(bg = self.colors[self.color_index])
        self.lbl2.config(bg = self.colors[self.color_index])
        self.color_index += 1
        if self.color_index >= len(self.colors):
            self.color_index = 0
  
    def activity(self):
        if self.total > 100:
            self.lbl3.config(text = "Activity: High ",fg = "green")
        elif self.total > 50:
            self.lbl3.config(text = "Activity: Medium",fg = "#f9a602")
        elif self.total < 50:
            self.lbl3.config(text = "Activity: Low",fg = "red")

  
def main():
    root = Tk()
    root.title("People in Store")
    root.geometry("200x171")
    root.resizable(0,0)
    root.attributes("-fullscreen",False)
    app = App(root)


    root.mainloop()

main()
