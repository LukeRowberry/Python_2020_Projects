from tkinter import *


HEIGHT = 800
WIDTH = 400
TITLE = "Order Up"
BACKGROUND = "darkgray"
FONT1 = "Times New Roman"#change?
FONT2 = "Courier" #change?



class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.total = DoubleVar
        self.total = 0.00
        Label(self, text="Italian Restaurant", font=(FONT1, 30)).grid(column=0,row=0, columnspan=2, rowspan=1, sticky=N)

        Label(self,text ="Appetizers",font=(FONT1,15)).grid(column = 0, row = 2,sticky = N)
        self.app1 = BooleanVar
        Checkbutton(self, text= "Ham and Egg",
                    variable=self.app1,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(column=0, row=3,sticky=N)
        Label(self, text= "$20.00").grid(column=1,row=3,sticky=N)
        self.app2 = BooleanVar
        Checkbutton(self, text= "Bacon and Cheese",
                    variable=self.app2,
                    font=(FONT2, 10),
                    command=self.update
                     ).grid(column=0, row=4,sticky=N)
        Label(self, text="10.00").grid(column=1, row=4, sticky=N)
        self.app3 = BooleanVar
        Checkbutton(self, text= "Tuna Salad",
                    variable=self.app3,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(column=0,row=5,sticky=N)
        Label(self, text="15.00").grid(column=1, row=5, sticky=N)
        self.app4 = BooleanVar
        Checkbutton(self, text="Beef Soup",
                    variable=self.app4,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(column=0,row=6,sticky=N)
        Label(self, text="25.00").grid(column=1, row=6, sticky=N)


        Label(self,text="Lunch",font=(FONT1,15)).grid(column=0, row=7, sticky=N)
        self.lun1 = BooleanVar()
        Checkbutton(self,
                    text = "Spicy Beef Barbecue",
                    variable = self.lun1,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(row = 8, column =0, sticky = N)
        Label(self, text="20.00").grid(column=1, row=8, sticky=N)
        self.lun2 = BooleanVar()
        Checkbutton(self,
                    text="Pork Barbecue",
                    variable=self.lun2,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(row=9, column=0, sticky=N)
        Label(self, text="$10.00").grid(column=1, row=9, sticky=N)
        self.lun3 = BooleanVar()
        Checkbutton(self,
                    text="Oven Chicken Barbecue",
                    variable=self.lun3,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(row=10, column=0, sticky=N)
        Label(self, text="$15.00").grid(column=1, row=10, sticky=N)
        self.lun4 = BooleanVar()
        Checkbutton(self,
                    text="Pulled Beef Barbecue Burger",
                    variable=self.lun4,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(row=11, column=0, sticky=N)
        Label(self, text="$25.00").grid(column=1, row=11, sticky=N)


        Label(self,text="Dinner",font=(FONT1,15)).grid(column=0, row=12, sticky=N)
        self.din1 = BooleanVar
        Checkbutton(self, text="Spicy Pork Barbecue",
                    variable=self.din1,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(column=0, row=13, sticky=N)
        Label(self, text="$20.00").grid(column=1, row=13, sticky=N)
        self.din2 = BooleanVar
        Checkbutton(self, text="Vegetable Pork Barbecue",
                    variable=self.din2,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(column=0, row=14, sticky=N)
        Label(self, text="$10.00").grid(column=1, row=14, sticky=N)
        self.din3 = BooleanVar
        Checkbutton(self, text="Oven Pork Barbecue",
                    variable=self.din3,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(column=0, row=15, sticky=N)
        Label(self, text="$15.00").grid(column=1, row=15, sticky=N)
        self.din4 = BooleanVar
        Checkbutton(self, text="Pulled Pork Barbecue",
                    variable=self.din4,
                    font=(FONT2, 10),
                    command=self.update
                    ).grid(column=0, row=16, sticky=N)
        Label(self, text="$25.00").grid(column=1, row=16, sticky=N)

        self.totalTxtLbl = Label(self, text=str.format("Total :")
                              ).grid(column=0, row=30, sticky=N)
        self.totalLbl = Label(self, text=str.format("${:.2f}", self.total)
                              ).grid(column=1, row=30, sticky=N)


    def update(self):
        self.total = 0.00
        self.items = [self.app1, self.app2, self.app3, self.app4,
                 self.lun1, self.lun2, self.lun3, self.lun4,
                 self.din1, self.din2, self.din3, self.din4]
        self.prices = [1.50, 2, 3, 4,
                  1, 2, 3, 4,
                  1, 2, 3, 4]
        for i in range(11):
            print(i)
            if self.items[i]:
                self.total += self.prices[i]
                print("if statement")



def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()
