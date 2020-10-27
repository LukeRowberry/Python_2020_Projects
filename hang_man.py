#Luke Rowberry
#10/9/2020
#Hangman Game
import random

HANGMAN = (
"""
------
|     |
|
|
|
|
|
|
----------
""",
"""
------
|     |
|     O
|
|
|
|
|
----------
""",
"""
------
|     |
|     O
|    -+-
|
|
|
|
----------
""",
"""
------
|     |
|     O
|    -+-\
|
|
|
|
----------
""",
"""
------
|     |
|     O
|   /-+-\
|
|
|
|
----------
""",
"""
------
|     |
|     O
|   /-+-\
|
|    |+|
|    |+|
|
----------
""",
"""
------
|     |
|     O
|   /-+-\
|
|    |+|
|    |+|
|
|
----------
"""
)
MAX_WRONG = len(HANGMAN)-1
WORDS = ("CLAM","TAFFETA","PYTHON","OVERUSED",) #must replace with python owrds later on
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
    print("\nSo far, the word is:\n",so_far)
else:
    print(HANGMAN[wrong])
    print("\nYou guessed the word!")
    print("\nSo far, the word is:\n",so_far)

input("\n\nPress the enter key to exit.")

    



##print(HANGMAN[len(HANGMAN)-1])
