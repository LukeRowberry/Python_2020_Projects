#Luke Rowberry
#10/1/2020
#Guess My Number 1.0

import random

theNumber = random.randint (1,10)

win = False 
print("\tWelcome to 'Guess My Number'!") 
print("\nI'm thinking of  number between 1 and 10.")
print("Try to guess it in 3 attempts.\n")


guess = int(input("Pick a number between 1 and 10. ")) #1

if guess == theNumber:
    print("Winner!")
    win = True
elif guess > theNumber:
    print("Guess lower!")
else:
    print("Guess higher!")

if win == False:
        guess = int(input("Pick a number between 1 and 10. ")) #2

        if (guess == theNumber) and (not win):
            print("Winner!")
            win = True
        elif guess > theNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

if win == False:
        guess = int(input("Pick a number between 1 and 10. ")) #3

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

