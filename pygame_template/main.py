import pygame
import random
import math
import os

#setup folder assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"images")
snd_folder = os.path.join(game_folder,"sounds")

HEIGHT = 360
WIDTH = 480
FPS = 30
title = "Template"
#For drap mouse movement
mouse_button_held = False

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
colors = [BLACK,WHITE,RED,BLUE,GREEN,YELLOW,PURPLE,ORANGE,PINK,BROWN,C_BLUE]

#Game Classes
class Npc(pygame.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        #self.rect.bottomright = (0,0)
        self.rect.center = (WIDTH/2,HEIGHT/2)
        #self.ang = 0
        self.speedx = 5
        self.speedy = 5
        #self.do_circle = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Bouncing movement
        if self.rect.right >= WIDTH-1 or self.rect.left <= 0:
            self.speedx *= -1
        if self.rect.top <= 1 or self.rect.bottom >= HEIGHT-1:
            self.speedy *= -1

        #Square movement
        # if self.rect.right >= WIDTH-1:
        #     self.speedx = 0
        #     self.speedy = -5
        # if self.rect.top <= 1:
        #     self.speedx = -5
        #     self.speedy = 0
        # if self.rect.left <= 1:
        #     self.speedx = 0
        #     self.speedy = 5
        # if self.rect.bottom >= HEIGHT-1:
        #     self.speedx = 5
        #     self.speedy = 0

        #Enemy movement pattern
        # if self.rect.centerx >= WIDTH/2 and self.ang < 360:
        #     self.do_circle = True
        #     if self.ang < 360:
        #         rad = self.ang * math.pi / 180
        #         self.rect.centery = -math.sin(rad) * 5 + self.rect.centery
        #         self.rect.centerx = math.cos(rad) * 5 + self.rect.centerx
        #         self.ang += 20
        #     else:
        #         self.do_circle = False
        # self.speedx = 5
        # self.speedy = -5
        # if self.rect.bottomleft[1] <= 0 and self.rect.bottomleft[1] > HEIGHT:
        #     self.rect.bottomright = (0,0)
        #     self.speedx = 5
        #     self.speedy = 5

        #V shape
        # if self.rect.centerx >= WIDTH/2:
        #     self.rect.speedx = 5
        #     self.rect.speedy = -5
        # if self.rect.bottomleft[1] <= 0 and self.rect.bottomleft[1] > HEIGHT:
        #     self.rect.bottomright = (0,0)

        #Screen wrapping
        # #Right
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        # #Left
        # if self.rect.right < 0:
        #     self.rect.left = WIDTH
        # #Up
        # if self.rect.top <0:
        #     self.rect.top = HEIGHT
        # #Down
        # if self.rect.top > HEIGHT:
        #     self.rect.top = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(PINK)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        #Mouse movement
        if mouse_button_held:
            self.rect.center = (mousex,mousey)

        #Basic movement
        # self.speedx = 0
        # self.speedy = 0
        # keystate = pygame.key.get_pressed()
        # if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
        #     self.speedx = -5
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
        #     self.speedx = 5
        # if keystate[pygame.K_UP] or keystate[pygame.K_w]:
        #     self.speedy = -5
        # if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
        #     self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Grid movement
        # keystate = pygame.key.get_pressed()
        # if (keystate[pygame.K_LEFT] or keystate[pygame.K_a]):
        #     self.rect.centerx += -50
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
        #     self.rect.centerx += 50
        # if keystate[pygame.K_UP] or keystate[pygame.K_w]:
        #     self.rect.centery += -50
        # if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
        #     self.rect.centery += 50

        #Borderwall
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

def spawn_new_player(x,y):
    new_player = Player()
    new_player.rect.center = (x,y)
    new_player.speedx = random.randint(-10, 10)
    new_player.speedy = random.randint(-10, 10)
    all_sprites.add(new_player)
    players_group.add(new_player)

#Initialize pygame and create window
pygame.init()
pygame.mixer.init()

#load game images
player_img = pygame.image.load(os.path.join(img_folder,"duck.png")).convert()


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title)

clock = pygame.time.Clock()

#Sprite Groups
all_sprites = pygame.sprite.Group()
players_group = pygame.sprite.Group()
mobs_group = pygame.sprite.Group()
#Create game objects
npc = Npc()
player = Player()
#Add objects to groups
all_sprites.add(npc)
mobs_group.add(npc)
all_sprites.add(player)
players_group.add(player)

#Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)

    mousex, mousey = pygame.mouse.get_pos()

    #process input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and player.rect.collidepoint(pygame.mouse.get_pos()):
            mouse_button_held = True
        if event.type == pygame.MOUSEBUTTONUP and mouse_button_held == True:
            mouse_button_held = False
            spawn_new_player(mousex, mousey)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT  or event.key == pygame.K_a or event.key == pygame.K_KP4:
        #         player.rect.x += -50
        #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP6:
        #         player.rect.x += 50
        #     if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP8:
        #         player.rect.y += -50
        #     if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_KP2:
        #         player.rect.y += 50
        #     if event.key == event.key == pygame.K_KP7:
        #         player.rect.x += -50
        #         player.rect.y += -50
        #     if event.key == event.key == pygame.K_KP9:
        #         player.rect.x += 50
        #         player.rect.y += -50
        #     if event.key == event.key == pygame.K_KP1:
        #         player.rect.x += -50
        #         player.rect.y += 50
        #     if event.key == event.key == pygame.K_KP3:
        #         player.rect.x += 50
        #         player.rect.y += 50

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #         player.speedx = -8
        #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #         player.speedx = 8
        #     if event.key == pygame.K_UP or event.key == pygame.K_w:
        #         player.speedy = -8
        #     if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        #         player.speedy = 8
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #         player.speedx = 0
        #     if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #         player.speedx = 0
        #     if event.key == pygame.K_UP or event.key == pygame.K_w:
        #         player.speedy = 0
        #     if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        #         player.speedy = 0
        #
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #update everything
    all_sprites.update()

    #render all changes
    screen.fill(C_BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()