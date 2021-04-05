import pygame as pg
import random
import os
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(PINK)
        self.image = pg.Surface((50,50))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.speedy = -5
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Borderwall
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
