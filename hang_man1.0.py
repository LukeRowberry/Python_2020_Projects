#Luke Rowberry
#10/9/2020
#Hangman Game 1.0
import random

HANGMAN = (
"""
-------
|     |
|  
|
|
|
|
----------
""",
"""
-------
|     |
|     O
|
|
|
|
----------
""",
"""
-------
|     |
|     O
|    -+-
|
|
|
----------
""",
"""
-------
|     |
|     O
|    -+-\\
|
|
|
----------
""",
"""
-------
|     |
|     O
|   /-+-\\
|
|
|
----------
""",
"""
-------
|     |
|     O
|   /-+-\\
|     +|
|     +|
|
----------
""",
"""
-------
|     |
|     O
|   /-+-\\
|    |+|
|    |+|
|
----------
"""
)
MAX_WRONG = len(HANGMAN)-1
WORDS = ("STRING",
         "PYTHON",
         "BOOLEAN",
         "INTEGER",
         "SYNTAX",
         "PRINT",
         "INPUT",
         "HASHTAG",
         "LOOP",
         "OPERATOR",) 

##word_index = random.randint(0,len(WORDS)-1)
##word = WORDS[word_index]
##print(word_index)

word = random.choice(WORDS)
so_far =  "-"*len(word)
used = [] 
wrong = 0

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
   
    print(so_far)

    print("\nYou've used the following letters:\n",used)

    guess = input("\nEnter your guess: ")
    guess = guess.upper()
    

    while guess in used:
        print("You've already guessed that letter",guess)
        guess = input("\nEnter your guess: ")
        guess = guess.upper()

    used.append(guess)
    

    if guess in word:
        print("\nYes!",guess,"is in the word!")
        #create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far = new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong+=1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
    print("\nSo far, you've guessed:",so_far)
    print("\nThe word was:",word)
else:
    print(HANGMAN[wrong])
    print("\nYou guessed the word!")
    print("\nThe word is:\n",so_far)

    if word == "STRING":
        print("""Defenition: Strings are lines of text that can be stored.""")
    elif word == "PYTHON":
        print("""Defenition: Python is the programming language
              that this program uses.""")
    elif word == "BOOLEAN":
        print("""Defenition: A boolean is a value that can store two possible values
              , True or False. Booleans are often used to make logical decisions.""")
    elif word == "INTEGER":
        print("""Defenition: Integers are values that can store whole numbers
              whether negative or positive.""")
    elif word == "SYNTAX":
        print("Defenition: Syntax are the rules of a language.")
    elif word == "PRINT":
        print("""Defenition: Print is a statement that will print
              and display whatever is within its own parenthesis.""")
    elif word == "INPUT":
        print("Defenition: Input is a value that stores user input.")
    elif word == "HASHTAG":
        print("""Defenition: Hashtags comment out regions of code and
              are not run as part of the code.""")
    elif word == "LOOP":
        print("""Defenition: Loops are parts are code that will continue to run
              forever until interupted.""")
    else:
        print("""Defenition: Operators are symbols that are used
              to perform operations on variables and values.""")


input("\n\nPress the enter key to exit...")

    



##print(HANGMAN[len(HANGMAN)-1])
