import random
import sys
from tkinter import *
from PIL import ImageTk,Image



class Cons():
    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27



class Board(Canvas):

    def __init__(self):
        super(Board, self).__init__(width = Cons.BOARD_WIDTH,
                                    height = Cons.BOARD_HEIGHT,
                                    background = "black",
                                    highlightthickness  = 0)
        self.initGame()
        self.pack()

    def initGame(self):
        """Initializes the game"""
        self.in_game = True
        self.dots = 3
        self.score = 0

        #variables used to make snake objct move
        self.moveX = Cons.DOT_SIZE
        self.moveY = 0

        #starting apple coordinates
        self.appleX = 100
        self.appleY = 190
  
        #Load images
        self.load_images()
        #Create game objects
        self.create_objects()
        #Place an apple on screen
        self.locate_apple()
        #Bind keyboard keys
        self.bind_all("<Key>",self.on_key_pressed)
        #Delay and timer of game
        self.after(Cons.DELAY,self.on_timer)

    def load_images(self):
        """Load images from files"""
        try:
            self.ibody = Image.open("images/body.png")
            self.ihead = Image.open("images/head.png")
            self.iapple = Image.open("images/apple.png")
            self.body = ImageTk.PhotoImage(self.ibody)
            self.head = ImageTk.PhotoImage(self.ihead)
            self.apple = ImageTk.PhotoImage(self.iapple)

        except IOError as e:
            print(e)
            sys.exit(1)
    def create_objects(self):
        """Create objects on Canvas"""
        self.create_text(30, 10, text = "Score = {0}".format(self.score),
                         tag = "score", fill = "white")
        self.create_image(self.appleX, self.appleY, image = self.apple, anchor = NW, tag = "apple")
        self.create_image(50, 50, image = self.head, anchor = NW, tag = "head")
        self.create_image(40, 50, image = self.body, anchor = NW, tag = "body")
        self.create_image(30, 50, image = self.body, anchor = NW, tag = "body")
    def locate_apple(self):
        """Place apple on Canvas"""
        apple = self.find_withtag("apple")
        self.delete(apple[0])
        r = random.randint(0,Cons.MAX_RAND_POS)
        self.appleX = r * Cons.DOT_SIZE
        r = random.randint(0,Cons.MAX_RAND_POS)
        self.appleY = r * Cons.DOT_SIZE

        self.create_image(self.appleX, self.appleY, anchor=NW, image=self.apple, tag="apple")
    def on_key_pressed(self,e):
        """Control direction with keys"""
        key = e.keysym
        LEFT_CURSOR_KEY = "Left"
        if key ==  LEFT_CURSOR_KEY and self.moveX <= 0:
            self.moveX = -Cons.DOT_SIZE
            self.moveY = 0
        RIGHT_CURSOR_KEY = "Right"
        if key ==  RIGHT_CURSOR_KEY and self.moveX >= 0:
            self.moveX = Cons.DOT_SIZE
            self.moveY = 0
        UP_CURSOR_KEY = "Up"
        if key ==  UP_CURSOR_KEY and self.moveX <= 0:
            self.moveX = 0
            self.moveY = -Cons.DOT_SIZE
        DOWN_CURSOR_KEY = "Down"
        if key ==  DOWN_CURSOR_KEY and self.moveX >= 0:
            self.moveX = 0
            self.moveY = Cons.DOT_SIZE
    def draw_score(self):
        score = self.find_withtag("score")
        self.itemconfigure(score, text = "Score: {0}".format(self.score))
    def check_collision(self):
        """Check for collisions"""
        body_parts = self.find_withtag("body")
        head = self.find_withtag("head")
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        for part in body_parts:
            for hit in overlap:
                if hit == part:
                    self.in_game = False

        if x1 < 0:
            self.in_game = False
        if x1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:
            self.in_game = False
        if y1 < 0:
            self.in_game = False
        if y1 > Cons.BOARD_HEIGHT - Cons.DOT_SIZE:
            self.in_game = False
    def move_snake(self):
        """Make snake move"""
        body_parts = self.find_withtag("body")
        head = self.find_withtag("head")
        snake_parts = body_parts + head

        z = 0
        while z < len(snake_parts)-1:
            c1 = self.coords(snake_parts[z])
            c2 = self.coords(snake_parts[z+1])
            self.move(snake_parts[z],c2[0]-c1[0],c2[1]-c1[1])
            z += 1
        self.move(head, self.moveX, self.moveY)
    def game_over(self):
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2,
                         text = "Game Over With A Score Of {0}".format(self.score), fill = "white")
    def check_apple_collision(self):
        apple = self.find_withtag("apple")
        head = self.find_withtag("head")
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        for hit in overlap:
            if apple[0] == hit:
                self.score += 1
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.body, anchor=NW, tag="body")
                self.locate_apple()
    def on_timer(self):
        """Create game cycle every tick"""
        self.draw_score()
        self.check_collision()
        if self.in_game:
            self.check_apple_collision()
            self.move_snake()
            self.after(Cons.DELAY, self.on_timer)
        else:
            self.game_over()
        
        
    
class Snake(Frame):

    def __init__(self, master):
        super(Snake, self).__init__(master)
        self.master.title("Snake Clone")
        self.board = Board()
        self.pack()



def main():
    root = Tk()
    snake = Snake(root)
    root.mainloop()
main()
    
    
    
    
