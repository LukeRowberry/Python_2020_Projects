import pygame as pg
import random
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (75, 0, 130)
ORANGE = (255, 69, 0)
PINK = (254, 127, 156)
BROWN = (139, 69, 19)
C_BLUE = (100, 149, 237)
colors = [BLACK,WHITE,RED,BLUE,GREEN,YELLOW,PURPLE,ORANGE,PINK,BROWN,C_BLUE]

HEIGHT = 360
WIDTH = 480
FPS = 60
title = "Name"

# Game Folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
snd_folder = os.path.join(game_folder, "sounds")