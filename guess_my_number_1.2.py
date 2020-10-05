#Luke Rowberry
#10/1/2020
#Guess My Number 1.2

import random
#settings
max_number = 10
num_trys = 3
diff = 1

win = False 
question = input("What difficulty would you like to play? (Easy,Medium,Hard) ")

if question == "Easy" or question == "easy" or question.startswith("E") or question.startswith("e"): 
    max_number = 10
    num_trys = 3
    diff = 1
elif question == "Medium" or question == "medium" or question.startswith("M") or question.startswith("m"):
    max_number = 50
    num_trys = 5
    diff = 2
else:
    max_number = 100
    num_trys = 10
    diff = 3

print("\tWelcome to 'Guess My Number'!") 
print(str.format("\nI'm thinking of  number between 1 and {}.",max_number))
print(str.format("Try to guess it in {} attempts.\n",num_trys))
theNumber = random.randint (1,max_number)




#1
guess = int(input("Pick a number between 1 and "+str(max_number)))

if guess == theNumber:
    print("Winner!")
    win = True
elif guess > theNumber:
    print("Guess lower!")
else:
    print("Guess higher!")

#2
if win == False:
        guess = int(input("Pick a number between 1 and "+str(max_number)))

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

#3
if win == False:
    if diff ==2 or diff ==3:
        guess = int(input("Pick a number between 1 and "+str(max_number)))

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

#4
if win == False:
    if diff ==2 or diff ==3:
        guess = int(input("Pick a number between 1 and "+str(max_number)))

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

#5
if win == False:
            if diff ==3:
                guess = int(input("Pick a number between 1 and "+str(max_number)))
                if (guess == theNumber) and (not win):
                    print("Winner!")
                    win = True
                elif guess > theNumber:
                    print("Guess lower!")
                else:
                    print("Guess higher!")

#6
if win == False:
    if diff ==3:
        guess = int(input("Pick a number between 1 and "+str(max_number)))
        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

#7
if win == False:
    if diff ==3:
        guess = int(input("Pick a number between 1 and "+str(max_number)))

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

#8
if win == False:
    if diff ==3:
        guess = int(input("Pick a number between 1 and "+str(max_number)))

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

#9
if win == False:
    if diff ==3:
        guess = int(input("Pick a number between 1 and "+str(max_number)))

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

#last guess
if win == False:
        guess = int(input("Pick a number between 1 and "+str(max_number)))

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("You lose!")
            print("The number was", theNumber)
        else:
            print("You lose!")
            print("The number was", theNumber)

if win:
    print("Great Job!")
else:
    print("Better luck next time!")

