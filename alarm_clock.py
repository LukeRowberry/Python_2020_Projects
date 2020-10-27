#currently broken

from tkinter import *
from tkinter import ttk
from tkinter import font
import calendar
import time
import datetime
import winsound

def gmtnow(alarm):
    """Getting Greenwich Mean Time"""

    seconds = calendar.timegm(time.gmtime())
    current_second =  seconds % 60

    minutes = seconds//60
    current_minute = minutes % 60

    hours = minutes//60
    current_hour = hours % 24

    current_hour -=6 #shorthand for current_hour = current_hour -6

    if current_hour >= 12:
        atag = "PM"
        current_hour -= 12
        if current_hour == 0:
            current_hour = 12
    else:
        atag = "AM"
        if current_hour == 0:
            current_hour = 12

    if current_hour < 10:
        adjusted_hour = "0"+str(current_hour)
    else:
        adjusted_hour = str(current_hour)

    if current_minute < 10:
        adjusted_minute = "0"+str(current_hour)
    else:
        adjusted_minute = str(current_hour)

    if current_second < 10:
        adjusted_second = "0"+str(current_hour)
    else:
        adjusted_second = str(current_hour)

    time_string = str.format("{:2}:{:2}:{:2},{}",adjusted_hour,adjusted_minute,adjusted_second,atag)
    
    print(time_string)
    return time_string

def show_time():
    time = gmtnow(alarm)
    txt.set(time)
    root.after(1000,show_time)

def alarm_snd():
    for i in range(5):
        winsound.Beep(750,1000)
        winsound.Beep(1000,500)
        winsound.Beep(750, 1000)

def alarm_input():
    ahour = input("What hour?")
    aminute = input("What minute?")
    asecond = input("00")
    atag = input("AM or PM").upper()
    if len(ahour) < 2:
        ahour = "0"+ahour
    if len(aminute) < 2:
         aminute = "0"+aminute
    alarm = str.format("{:2}:{:2}:{:2},{}",ahour,aminute,asecond,atag)

    print(time_string)
    if alarm == time_string:
        alarm_snd()

    return time_string
alarm = alarm_input()

root = Tk()
root.geometry("800x200")
root.attributes("-fullscreen", False)
root.configure(background = "black")
root.bind("x", quit)
root.after(1000,show_time)
fnt = font.Font(family = "Century Gothic",size = 60,weight = "normal")
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt,foreground = "white",background = "black")
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()

gmtnow()
