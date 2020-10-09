#Luke Rowberry
#10/9/2020
#Hangman Game
import random

HANGMAN = (
"""
------
|      |
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
|      |
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
|      |
|     O
|   -+-
|
|
|
|
----------
""",
"""
------
|      |
|     O
|   -+-\
|
|
|
|
----------
""",
"""
------
|      |
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
|      |
|     O
|   /-+-\
|
|     |+
|     |+
|
----------
""",
"""
------
|      |
|     O
|   /-+-\
|
|     |+|
|     |+|
|
|
----------
"""
)
MAX_WRONG = len(HANGMAN)-1
WORDS = ("clam","taffeta","python","overused",) #must replace with python owrds later on
##word_index = random.randint(0,len(WORDS)-1)
##word = WORDS[word_index]
##print(word_index)

word = random.choice(WORDS)
so_far =  "- "*len(word)
used = [] 
wrong= 0

print("Welcome to Hangman. Good luck!")
print(HANGMAN[0])
print()
print(so_far)

##print(HANGMAN[len(HANGMAN)-1])
