import pygame as pg
import random as r
import math
from os import *

#Attribution
########################################################################
#Code by: Luke Rowberry
#Credit artwork by: "Kenney.nl" or "www.kenney.nl"
########################################################################



#Classes
########################################################################
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.image = pg.Surface((50,40))
        # self.image.fill(PURPLE)
        self.image = player_img
        self.image = pg.transform.scale(player_img,(50,40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        pg.draw.circle(self.image, RED, self.rect.center, self.radius)
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
        # self.image = pg.Surface((5, 10))
        # self.image.fill(YELLOW)
        self.image = player_img
        self.image = pg.transform.scale(laser_img, (10, 30))
        self.image.set_colorkey(BLACK)
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
        # self.image = pg.Surface((25,25))
        # self.image.fill(RED)
        self.image = npc_image
        self.image = pg.transform.scale(npc_image, (40, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.75/2)
        pg.draw.circle(self.image, RED, self.rect.center,self.radius)
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



#Folder Variables
########################################################################
game_folder = path.dirname(__file__)
images_folder = path.join(game_folder,"images")
sounds_folder = path.join(game_folder,"sounds")
scores_folder = path.join(game_folder,"scores")
player_img_folder = path.join(images_folder,"player_images")
enemy_img_folder = path.join(images_folder,"enemy_images")
background_img_folder = path.join(images_folder,"background_images")
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
#Background
background = pg.image.load(path.join(background_img_folder,"starfield.png")).convert()
background_rect = background.get_rect()
background = pg.transform.scale(background,(WIDTH,HEIGHT))
#Player
player_img = pg.image.load(path.join(player_img_folder,"playership1.png")).convert()
#Asteroid
npc_image = pg.image.load(path.join(enemy_img_folder,"meteor.png")).convert()
#Laser
laser_img = pg.image.load(path.join(player_img_folder,"laser.png")).convert()
########################################################################



#Sprite Groups
########################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
########################################################################



#Create Game Objects
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
    hits = pg.sprite.spritecollide(player,npc_group,True,pg.sprite.collide_circle)
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
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    pg.display.flip()
    ###########################################
###########################################################
###########################################################
pg.quit()
########################################################################