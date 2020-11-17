#Tic-Tac-Toe
#Luke Rowberry
#Playing tic-tac-toe against an AI
#11-13-2020

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#functions that call in main
def display_instruct():
    """Display game instructions. To use type (display_instruct())"""

    print("""
    Welcome to the greateest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0 - 8. The number
    will correspond to the board position as illustrated:

                                        0 | 1 | 2
                                        ---------
                                        3 | 4 | 5
                                        ---------
                                        6 | 7 | 8

    Prepare youself, human. The ultimate battle is about to begin. \n
    """)

def next_turn(turn):
    """This function switches the players' turn. To use type (turn = next_turn(turn))"""
    if turn == X:
        return O
    else:
        return X

def pieces():
    """Assigns  which player goes first. To use type (computer, human = pieces())"""
    go_first = ask_yes_no("Do you want to go first?  (y/n):  ")
    if go_first == "y" or go_first == "yes":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        human = O
        computer = X
    return computer, human
        

def ask_yes_no(questions):
    """Ask a yes or no question and get back a yes or no answer. To use (answer = ask_yes_no(question))"""
    response = None
    while response not in ("y", "n", "yes", "no"):
        response = input(questions).lower()
    return response

def new_board():
    """Create a new game board. To use type (board = new_board())"""
    board = []
    for square in range (NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display game board on screen. To use type (display_board(board))"""
    print("\t",board[0]," | ",board[1]," | ",board[2])
    print("\t", "---------")
    print("\t",board[3]," | ",board[4]," | ",board[5])
    print("\t", "---------")
    print("\t",board[6]," | ",board[7]," | ",board[8])

def human_move(board,human):
    """Get a human move. To use type (move = human_move(board, human))"""
    move = None
    while move == None:
        move = ask_number("Where will you move?  (0 - 8):  ", 0, NUM_SQUARES)
    return move

def ask_number(question, low, high):
    """Ask for a number within a range. To use type (answer = ask_number(question, low, high))"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response




############################################


#main game
def main():
    display_instruct()
    turn = X
    computer, human = pieces()
    print(computer, human)
    board = new_board()
    print (board)
    while True:
        display_board(board)
        move = human_move(board, human)
        board[move] = human
    
main()

