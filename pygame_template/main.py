import pygame
import random
import math

HEIGHT = 360
WIDTH = 480
FPS = 30
title = "Template"

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
        self.image = pygame.Surface((50, 50))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def  update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Right
        if self.rect.left > WIDTH:
            self.rect.right = 0
        #Left
        if self.rect.right < 0:
            self.rect.left = WIDTH
        #Up
        if self.rect.top <0:
            self.rect.top = HEIGHT
        #Down
        if self.rect.top > HEIGHT:
            self.rect.top = 0

#Initialize pygame and create window
pygame.init()
pygame.mixer.init()


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
    #process input
    for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player.rect.x += -50
        #     if event.key == pygame.K_RIGHT:
        #         player.rect.x += 50
        #     if event.key == pygame.K_UP:
        #         player.rect.y += -50
        #     if event.key == pygame.K_DOWN:
        #         player.rect.y += 50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx = -8
            if event.key == pygame.K_RIGHT:
                player.speedx = 8
            if event.key == pygame.K_UP:
                player.speedy = -8
            if event.key == pygame.K_DOWN:
                player.speedy = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx = 0
            if event.key == pygame.K_RIGHT:
                player.speedx = 0
            if event.key == pygame.K_UP:
                player.speedy = 0
            if event.key == pygame.K_DOWN:
                player.speedy = 0


        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #update everything
    all_sprites.update()

    #render all changes
    screen.fill(C_BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()