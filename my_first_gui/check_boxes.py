from tkinter import *

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Choose Your Favorite Types Of Foods")
        self.title.grid(columnspan=2, sticky=N)

        self.select = Label(self, text="Select All That Apply")
        self.select.grid(row=1, sticky=W)

        self.lbl1 = Label(self, text="lbl1")
        self.lbl1.grid(row=2, column=1, sticky=W)

        self.lbl2 = Label(self, text="lbl2")
        self.lbl2.grid(row=3, column=1, sticky=W)

        self.lbl3 = Label(self, text="lbl3")
        self.lbl3.grid(row=4, column=1, sticky=W)

        self.output = Text(self)
        self.output.grid(row=8, columnspan=2)

        self.name = Label(self, text="Name")
        self.name.grid(row=2, sticky=W)

        self.text_name = Entry(self)
        self.text_name.grid(row=2, column=1, columnspan=2, sticky=W)

        self.likes_pizza = BooleanVar()
        Checkbutton(self,
                    text = "Pizza",
                    variable = self.likes_pizza,
                    command = self.update
                    ).grid(row = 2, column =0, sticky = W)
        self.likes_tacos = BooleanVar()
        Checkbutton(self,
                    text="Tacos",
                    variable=self.likes_tacos,
                    command=self.update
                    ).grid(row=3, column=0, sticky=W)
        self.likes_hotdogs = BooleanVar()
        Checkbutton(self,
                    text="Hotdogs",
                    variable=self.likes_hotdogs,
                    command=self.update
                    ).grid(row=4, column=0, sticky=W)

        self.worst_food = StringVar()
        self.worst_food.set(None)
        Radiobutton(self,
                    text = "Tomato",
                    value = "Tomato",
                    variable = self.worst_food,
                    command=self.update
                    ).grid(row = 5, column = 0,sticky = W)
        Radiobutton(self,
                    text="Beets",
                    value="Beets",
                    variable=self.worst_food,
                    command=self.update
                    ).grid(row=6, column=0,sticky = W)
        Radiobutton(self,
                    text="Food",
                    value="Food",
                    variable=self.worst_food,
                    command=self.update
                    ).grid(row=7, column=0,sticky = W)



    def update(self):
        likes = ""
        if self.likes_pizza.get():
            likes += "You like pizza\n"
        if self.likes_tacos.get():
            likes += "You like tacos\n"
        if self.likes_hotdogs.get():
            likes += "You like hotdogs\n"
        likes += "Your least favorite food is "+self.worst_food.get()

        self.output.delete(0.0,END)
        self.output.insert(0.0,likes)

def main():
    root = Tk()
    root.title("Title")
    root.geometry("650x500")
    app = App(root)
    root.mainloop()
main()