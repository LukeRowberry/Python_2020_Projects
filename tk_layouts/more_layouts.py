from tkinter import *
from tkinter.ttk import *
HEIGHT = 250
WIDTH = 250
TITLE = "New Program"

class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.pack(fill=X)
        self.create_widgets()

    def create_widgets(self):
        self.items_list = [1,2,3,4,5,"string1"]
        self.combo_box = Combobox(self, values = self.items_list) #option 1
        #self.combo_box.config(values = items_list) #option 2
        #self.combo_box["values"]=items_list #option 3
        self.combo_box.current(None)
        self.combo_box.pack(side = LEFT)

        self.submit = Button(self, text = "Try Me",command = self.on_change_values)
        self.submit.pack()

        list_items = ["test1","test2","test3","test4"]
        self.list_box = Listbox(self)
        for i in range(len(list_items)):
            self.list_box.insert(i,list_items[i])
            self.list_box.pack(side = LEFT)

        self.increase = Button(self,text = ">>>>>", command = self.inc)
        self.decrease = Button(self,text = "<<<<<", command = self.dec)
        self.increase.pack(side = LEFT)
        self.decrease.pack(side = LEFT)
                               
        self.progressbar = Progressbar(self,length = 200, value = 5)
        self.progressbar.pack(side = LEFT)

    def inc(self):
        self.progressbar["value"]=self.progressbar["value"]+1
    def dec(self):
        self.progressbar["value"]=self.progressbar["value"]-1

    def on_change_values(self):
        cbtext = self.combo_box.get()
        print(cbtext)
        self.list_box.insert(END,cbtext)
        
        self.lbtext = self.list_box.get(ANCHOR) #Use "ALL" to select all
        print(self.lbtext)
        self.items_list.append(self.lbtext)
        self.combo_box["values"]= self.items_list


        
root = Tk()
root.title(TITLE)
#root.geometry(str(WIDTH)+"x"+str(+HEIGHT))
app = App(root)

root.mainloop()
