#Luke Rowberry
#12,3,2020
#Test that can read plain text files

#imports
import sys
from datetime import datetime

#functions
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



def next_question(file):
    """return the next question block from trivia file."""
    category = next_line(file)
    question = next_line(file)
    answers = []
    for i in range(4):
        answers.append(next_line(file))
    correct = next_line(file)

    if correct:
        correct = correct[0]
    explaination = next_line(file)
    return category, question, answers, correct, explaination



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



def welcome(title,name,test_time):
    """welcomes the player."""
    print("Welcome "+name+" to your Mid-Term Test\n")
    print("Your tester is "+title)



def create_report_card(name,score,total_questions,test_time):
    """student report card"""
    card = open("assets/scores/"+name+".txt","w")
    card.write("Student Name: "+name+"\n")
    casrd.write("Date Taken: "+test_time+"\n")
    card.write("Amount Correct: "+str(score)+"\n")
    percentage = score/total_questions*100
    card.write("Percentage Score: "+"%"+str(percentage)+"\n")
    if percentage >= 90:
        card.write("Letter Grade: A")
    elif percentage >= 80 and percentage < 90:
        card.write("Letter Grade: B")
    elif percentage >= 70 and percentage < 80:
        card.write("Letter Grade: C")
    elif percentage >= 60 and percentage < 70:
        card.write("Letter Grade: D")
    elif percentage <= 60:
        card.write("Letter Grade: F")
    card.close()
    
    
        


def main():
    file = open_file("example_test.txt","r") #will need to change file name to match the test that your taking
    title = next_line(file)
    name,test_time = get_name()
    welcome(title,name,test_time)
    score = 0
    total_questions = 0
    category, question, answers, correct, explaination = next_question(file)
    while category:
        total_questions += 1
        print(category)
        print(question)
        for i in range(len(answers)):
            print(str.format("\t{}:  {}",i+1,answers[i]))
        #get answer from user
        answer = input("Type in your answer: ")
        #check if answer is correct
        if answer == correct:
            print("\nThat's Correct!", end=" ")
            score +=1
            print("Score: ", score, "\n\n")
            category, question, answers, correct, explaination = next_question(file)
        else:
            print("\nThat's Wrong!", end=" ")
            print(explaination)
            print("Score: ", score, "\n\n")
            #get next question
            category, question, answers, correct, explaination = next_question(file)
    file.close()
    print("That was the last question!")
    print("Your final score is...", score)
    create_report_card(name,score,total_questions,test_time)
            
          
main()
