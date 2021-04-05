#Pygame template - skeleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from sprites import *

class Game(object):
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()

    def new(self):
        #Create Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.players_group = pg.sprite.Group()
        self.mobs_group = pg.sprite.Group()

        #Create Game Objects
        self.player = Player()

        #Add Game Objects to Groups
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        #Game Loop - Updates
        self.all_sprites.update()

    def draw(self):
        #Game Loop - Draw
        self.screen.fill(C_BLUE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def game_over(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.game_over()
pg.quit()
