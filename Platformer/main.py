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
        self.platforms = pg.sprite.Group()
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        #Create Game Objects
        self.player = Player(self)

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
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def update(self):
        #Game Loop - Updates
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def draw(self):
        #Game Loop - Draw
        self.screen.fill(BLACK)
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
