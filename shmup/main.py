import pygame as pg
import random as r
import math
from os import *

#Classes
########################################################################
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50,40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.centery = (HEIGHT - (HEIGHT*.05))
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pg.Surface((25,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.top = (0)
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = 0
########################################################################



#Game Constants
########################################################################
HEIGHT = 900
WIDTH = 600
FPS = 60

#Colors (R,G,B)
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

title = "Shmup"
########################################################################



#Initialize Pygame and Create Window
########################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
########################################################################



#Load Images
########################################################################

########################################################################



#Sprite Groups
########################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
########################################################################



#Creat Game Objects
########################################################################
player = Player()
npc = Npc()
########################################################################



#Add Objects to Sprite Groups
########################################################################
players_group.add(player)
npc_group.add(npc)
for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)
########################################################################



#Game Loop
########################################################################

#Game Update Variables
###########################################################
playing = True
###########################################################
###########################################################
while playing:
    #Timing
    ###########################################
    clock.tick(FPS)
    ###########################################

    #Collect Input
    ###########################################
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
    ###########################################

    #Updates
    ###########################################
    all_sprites.update()
    ###########################################

    #Render/Draw
    ###########################################
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()
    ###########################################
###########################################################
###########################################################
pg.quit()
########################################################################