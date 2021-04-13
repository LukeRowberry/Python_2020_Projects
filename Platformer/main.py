#Pygame template - skeleton for a new pygame project

#Credits
#Art by Kenney.nl
#Happy Tune by http://opengameart.org/users/syncopika
#Yippee by http://opengameart.org/users.snabisch

import pygame as pg
import random
import os
from settings import *
from sprites import *
from os import path

class Game(object):
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        #Load highscores
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE),"r") as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        #Load Spritesheet
        img_dir = path.join(self.dir, "images")
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        #Load Sounds
        self.sound_dir = path.join(self.dir, "sounds")
        self.jump_sound = pg.mixer.Sound(path.join(self.sound_dir, "Jump33.wav"))
        self.boost_sound = pg.mixer.Sound(path.join(self.sound_dir, "Boost16.wav"))

    def new(self):
        #Create Sprite Groups
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.player = Player(self)
        for plat in PLATFORM_LIST:
            Platform(self, *plat)
        pg.mixer.music.load(path.join(self.sound_dir, "Happy Tune.ogg"))
        self.run()

    def run(self):
        #Game Loop
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(loops = -1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)

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
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def update(self):
        #Game Loop - Updates
        self.all_sprites.update()
        #Check if player hits a platform - falling only
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right + 10 and \
                self.player.pos.x > lowest.rect.left - 10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False

        #If player hits powerup
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
        for pow in pow_hits:
            if pow.type == "boost":
                self.boost_sound.play()
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False

        #Death
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += max(abs(self.player.vel.y), 3)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 3)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        #Platform Generation
        while len(self.platforms) < 5:
             width = random.randrange(50,100)
             p = Platform(self, random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30))

        #If player reaches 1/4 of screen
        if self.player.rect.top > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False


    def draw(self):
        #Game Loop - Draw
        self.screen.fill(C_BLUE)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.draw_text(str(self.score), 22, WHITE, WIDTH/2, 15)
        pg.display.flip()

    def show_start_screen(self):
        pg.mixer.music.load(path.join(self.sound_dir, "Yippee.ogg"))
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(loops = -1)
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE,48,WHITE,WIDTH/2,HEIGHT/4)
        self.draw_text("Use the ARROW keys to move",22,WHITE,WIDTH/2,HEIGHT/2-40)
        self.draw_text("Use the SPACEBAR to jump", 22, WHITE, WIDTH / 2, HEIGHT/2)
        self.draw_text("Press ANY key to play",22,WHITE,WIDTH/2,HEIGHT*3/4)
        self.draw_text("High Score: "+str(self.highscore),22,WHITE,WIDTH/2,HEIGHT/2+40)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def game_over(self):
        if not self.running:
            return
        pg.mixer.music.load(path.join(self.sound_dir, "Yippee.ogg"))
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: "+str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press ANY key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!",22,WHITE,WIDTH/2,HEIGHT/2+40)
            with open(path.join(self.dir,HS_FILE), "w") as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT/2+40)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.game_over()
pg.quit()
