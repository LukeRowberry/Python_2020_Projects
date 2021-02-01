from tkinter import *

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_cb(self,words,ischecked,commandcall,r,c,cs = 1,rs = 1):
        self.ischecked = BooleanVar()
        Checkbutton(self,
                    text= words,
                    variable= ischecked,
                    command= commandcall
                    ).grid(row= r, column=c,columnspan = cs,rowspan = rs)


    def create_widgets(self):

        # self.pep = BooleanVar()
        # self.sau = BooleanVar
        # self.boolsvars = [self.pep,self.sau,self.pep,self.sau,self.pep,self.sau,self.pep,self.sau,self.pep,self.sau,self.pep,self.sau,]
        # self.topp = ["Pep_roni","Sau_sage""Pep_roni","Sau_sage""Pep_roni","Sau_sage""Pep_roni","Sau_sage""Pep_roni","Sau_sage""Pep_roni","Sau_sage"]
        # for r in range(4):
        #     for c in range(3):
        #         self.create_cb(self.topp[c],self.boolsvars[c],self.update,17+r,c)

        self.title = Label(self, text="Your Pizza Order")
        self.title.grid(columnspan=2, sticky=N)

        self.size = Label(self, text="Choose your Size:")
        self.size.grid(row=5, sticky=W)

        self.size = Label(self, text="Choose your Crust:")
        self.size.grid(row=7, sticky=W)

        self.lbl_toppings = Label(self, text="Choose your Toppings:")
        self.lbl_toppings.grid(row=10, sticky=W)

        self.output = Text(self,width = 50, height = 20)
        self.output.grid(row=15, columnspan=3)

        self.name = Label(self, text="Name:")
        self.name.grid(row=2, sticky=W)

        self.text_name = Entry(self)
        self.text_name.grid(row=2, column=1, columnspan=2, sticky=W)

        self.address = Label(self, text="Address:")
        self.address.grid(row=3, sticky=W)

        self.text_address = Entry(self)
        self.text_address.grid(row=3, column=1, columnspan=2, sticky=W)

        self.phone = Label(self, text="Phone Number:")
        self.phone.grid(row=4, sticky=W)

        self.text_phone = Entry(self)
        self.text_phone.grid(row=4, column=1, columnspan=2, sticky=W)

        self.bttn = Button(self, text="Submit")
        self.bttn.grid(row=16,columnspan=3)

        self.select_size = StringVar()
        self.select_size.set(None)
        Radiobutton(self,
                    text="Small",
                    value="Small",
                    variable=self.select_size,
                    command=self.update
                    ).grid(row=6, column=0, sticky=W)
        Radiobutton(self,
                    text="Medium",
                    value="Medium",
                    variable=self.select_size,
                    command=self.update
                    ).grid(row=6, column=1, sticky=W)
        Radiobutton(self,
                    text="Large",
                    value="Large",
                    variable=self.select_size,
                    command=self.update
                    ).grid(row=6, column=2, sticky=W)

        self.select_crust = StringVar()
        self.select_crust.set(None)
        Radiobutton(self,
                    text="Original",
                    value="Original",
                    variable=self.select_crust,
                    command=self.update
                    ).grid(row=8, column=0, sticky=W)
        Radiobutton(self,
                    text="Thin",
                    value="Thin",
                    variable=self.select_crust,
                    command=self.update
                    ).grid(row=8, column=1, sticky=W)
        Radiobutton(self,
                    text="Deep",
                    value="Deep",
                    variable=self.select_crust,
                    command=self.update
                    ).grid(row=8, column=2, sticky=W)
        Radiobutton(self,
                    text="Stuffed",
                    value="Stuffed",
                    variable=self.select_crust,
                    command=self.update
                    ).grid(row=9, column=0, sticky=W)
        Radiobutton(self,
                    text="Gluten-Free",
                    value="Gluten-Free",
                    variable=self.select_crust,
                    command=self.update
                    ).grid(row=9, column=1, sticky=W)
        Radiobutton(self,
                    text="No Crust",
                    value="No Crust",
                    variable=self.select_crust,
                    command=self.update
                    ).grid(row=9, column=2, sticky=W)

        self.pepperoni = BooleanVar()
        self.cheese = BooleanVar()
        self.pineapple = BooleanVar()
        self.olive = BooleanVar()
        self.spinach = BooleanVar()
        self.onion = BooleanVar()
        self.sausage = BooleanVar()
        self.bacon = BooleanVar()
        self.mushroom = BooleanVar()
        self.chicken = BooleanVar()
        self.ham = BooleanVar()
        self.jalapeno = BooleanVar()
        self.boolsvars = [self.pepperoni, self.cheese, self.pineapple, self.olive, self.spinach, self.onion,
                          self.sausage, self.bacon, self.mushroom, self.chicken, self.ham, self.jalapeno]
        self.toppings = ["Pepperoni", "Cheese", "Pineapple", "Olive", "Spinach", "Onion", "Sausage", "Bacon",
                         "Mushroom", "Chicken", "Ham", "Jalapeno"]
        for r in range(4):
            for c in range(3):
                self.create_cb(self.toppings[c], self.boolsvars[c], self.update, 11 + r, c)

    def update(self):
        order = "Your order includes:\n"
        order += "\nSize: "+self.select_size.get()
        order += "\nCrust: " + self.select_crust.get()
        order += "\nToppings: \n"
        if self.pepperoni.get():
            order += "Pepperoni\n"
        if self.cheese.get():
            order += "Cheese\n"
        if self.pineapple.get():
            order += "Pineapple\n"
        if self.olive.get():
            order += "Olive\n"
        if self.spinach.get():
            order += "Spinach\n"
        if self.onion.get():
            order += "Onion\n"
        if self.sausage.get():
            order += "Sausage\n"
        if self.bacon.get():
            order += "Bacon\n"
        if self.mushroom.get():
            order += "Mushroom\n"
        if self.chicken.get():
            order += "Chicken\n"
        if self.ham.get():
            order += "Ham\n"
        if self.jalapeno.get():
            order += "Jalapeno\n"
        order += "\nName: "+self.text_name.get()
        order += "\nAddress: " + self.text_address.get()
        order += "\nPhone Number: " + self.text_phone.get()


        self.output.delete(0.0,END)
        self.output.insert(0.0,order)


def main():
    root = Tk()
    root.title("Pizza Order")
    root.geometry("410x680")
    app = App(root)
    root.mainloop()
main()