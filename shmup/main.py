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

    def shoot(self):
        b = Bullet(self.rect.centerx,self.rect.top + 1)
        all_sprites.add(b)
        bullet_group.add(b)

    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        #Ship stays on screen
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        #Ship shoots bullet
        #if keystate[pg.K_SPACE]:
        #    self.shoot()


class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        self.image = pg.Surface((5, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pg.Surface((25,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = r.randrange(-100, -40)
        self.speedy = r.randrange(1, 8)
        self.speedx = r.randrange(-3, 3)

    def spawn(self):
        npc = Npc()
        npc_group.add(npc)
        all_sprites.add(npc)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = r.randrange(WIDTH - self.rect.width)
            self.rect.y = r.randrange(-100, -40)
            self.speedy = r.randrange(1, 8)
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
bullet_group = pg.sprite.Group()
########################################################################



#Creat Game Objects
########################################################################
player = Player()

for i in range(10):
    npc = Npc()
    npc_group.add(npc)
########################################################################



#Add Objects to Sprite Groups
########################################################################
players_group.add(player)

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
            if event.key == pg.K_SPACE:
                player.shoot()
            if event.key == pg.K_ESCAPE:
                playing = False
    ###########################################

    #Updates
    ###########################################
    all_sprites.update()
    #Npc hits player
    hits = pg.sprite.spritecollide(player,npc_group,True)
    if hits:
        #playing = False ----this is here----
        npc.spawn()
    #Bullet hits Npc
    hits = pg.sprite.groupcollide(npc_group,bullet_group, True, True)
    for hit in hits:
        npc.spawn()
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