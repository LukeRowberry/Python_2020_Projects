import pygame as pg

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
BROWN2 = (106, 55, 5)
C_BLUE = (100, 149, 237)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)

#Game Settings
HEIGHT = 768
WIDTH = 1024
FPS = 60
TITLE = "Tile_Based Demo"
BG_COLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = "tileGreen_38.png"

#Player Settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

#Mob Settings
MOB_IMG = "zoimbie1_hold.png"
