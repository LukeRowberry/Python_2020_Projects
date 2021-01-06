import sys
from datetime import datetime


def menu(options):       #menu function
    index = 1
    for i in options:
        print (str.format("[{}: ........ {:.50}]",index,i))
        index+=1
    while True:
        choice = input("Pick a number between 1 and "+str(len(options)))
        if choice.isnumeric():
            choice = int(choice)
            if choice >= 1 and choice <= len(options):
                return choice
            else:
                print("Not a good option")
        else:
            print("Not a good option")

def getnum(question,low,high):
    while True:
        num = input(question)
        if num.isnumeric():
            num = int(num)
            if num >= low and num <= high:
                return num
        print("not a valid number")

def get_name():
    """get the name and the date taken."""
    try:
        time = datetime.now()
        test_time = time.strftime("%m/%d %H:%M")
        while True:
            name = input("Please enter your name: ")
            if (len(name) >= 3) and (" " in name):
                name = name.title()
                return name, test_time
            else:
                print("Not a valid option...")
    except:
        print("Something went wrong while getting name")
        sys.exit()

def open_file(file_name,mode):
    """open and returns an open file with the given permissions."""
    try:
        file = open("assets/test_files/"+file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name,"Ending program. \n", e)
        try:
            file = open("assets/errors/errors_log.txt","a+")
            time = datetime.now()
            error_time = time.strftime("%m/%d/%Y %H:%M:%S")
            file.write(str(e)+" "+str(error_time)+"\n")
            input("\n\nPress ENTER to exit...")
            sys.exit()
        except:
            sys.exit()
    else:
        return file

def next_line(file):
    """reads next line in trivia file."""
    try:
        line = file.readline()
        line = line.replace("/","\n")
        return line
    except:
        print("Couldn't read line...")
        sys.exit()


def ask_yes_no(questions):
    """Ask a yes or no question and get back a yes or no answer. To use (answer = ask_yes_no(question))"""
    response = None
    while response not in ("y", "n", "yes", "no"):
        response = input(questions).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range. To use type (answer = ask_number(question, low, high))"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = Score()
        self.lives = 3

class Score(object):
    def __init__(self):
        self.value = 0
        self.stepvalue = 10
    def add_to(self,itemid):
        for i in range(itemid):
            self.value += self.stepvalue
    def take_from(self,itemid):
        for i in range(itemid):
            self.value -= self.stepvalue
            if self.value < 0:
                self.value = 0

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the ENTER key to exit.")