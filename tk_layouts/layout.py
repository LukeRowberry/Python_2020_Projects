# Luke Rowberry
# 2-3-2021
# Layouts
from tkinter import *
from PIL import Image, ImageTk
HEIGHT = 750
WIDTH = 250



class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.index = 0
        self.index2 = 1
        self.index3 = 2
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        self.config(bg="DarkGrey")
        Label(text="my favorite image", width=20).place(x=WIDTH / 2 - 70, y=5)

        img1 = Image.open("pie.jpg")
        img2 = Image.open("toilet.jpg")
        img3 = Image.open("salad.jpg")

        logo1 = ImageTk.PhotoImage(img1)
        logo2 = ImageTk.PhotoImage(img2)
        logo3 = ImageTk.PhotoImage(img3)
        self.imglist = [logo1,logo2,logo3]

        self.imglbl1 = Label(self,image = self.imglist[0])
        self.imglbl1.image = logo1
        self.imglbl1.place(x=25,y=75)

        self.imglbl2 = Label(self, image=self.imglist[1])
        self.imglbl2.image = logo2
        self.imglbl2.place(x=25, y=240)

        self.imglbl3 = Label(self, image=self.imglist[2])
        self.imglbl3.image = logo3
        self.imglbl3.place(x=25, y=400)

        bttn1 = Button(self,text = "Change",command = self.change_img)
        bttn1.place(x=25,y=650)

    def change_img(self):
        self.index += 1
        self.index2 += 1
        self.index3 += 1

        if self.index >= len(self.imglist):
            self.index = 0
        self.imglbl1.config(image=self.imglist[self.index])

        if self.index2 >= len(self.imglist):
            self.index2 = 0
        self.imglbl2.config(image=self.imglist[self.index2])

        if self.index3 >= len(self.imglist):
            self.index3 = 0
        self.imglbl3.config(image=self.imglist[self.index3])




root = Tk()
root.title("Images")
root.geometry(str(WIDTH) + "x" + str(+HEIGHT))
app = App(root)

root.mainloop()