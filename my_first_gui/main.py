#Simple Gui
#Demonstrates creating a window
from tkinter import *

root = Tk()
#window title
root.title("Luke's Gui")
#window size
root.geometry("720x719")
#makes window unresizeable
root.resizable(0,0)
#makes window fullscreen
#root.attributes("-fullscreen",True)
#background color
root.configure(bg = "#630436")

#create Frame to place widgets on
app = Frame(root)
app.grid()

app2 = Frame(root)
app2.grid()
lbl2 = Label(app2,text = "BIG", bg = "blue", fg = "red",font = ("Sans",30,"bold"))
lbl2.grid()

#create label
lbl = Label(app,text = "There is text", bg = "yellow", fg = "blue",font = ("Sans",50,"bold"))
#lbl.config(font = ("Sans", 90,"bold"))

#puts label on the grid
lbl.grid()

#create some buttons
bttn1 = Button(app,text = "good boy")
bttn1.grid()
bttn2 = Button()
bttn2.grid()

for i in range(5):
    x = Button(app)
    x["text"] = "button"+str(i+1)
    x.grid()

    x.config(bg="green")

bttn2.config(text = "bad boy", bg = "red", fg = "green")




#kick off the windows event loop
root.mainloop()
