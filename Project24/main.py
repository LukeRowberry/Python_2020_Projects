import pygame as pg
import math
import random
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.vx,self.vy = 0,0
        keystate = pg.key.get_pressed()
        # sum = 0
        # for i in keystate:
        #     sum += i
        # if sum <= 1:
        if keystate[pg.K_UP]:
            self.vy = -5
        if keystate[pg.K_DOWN]:
            self.vy = 5
        if keystate[pg.K_LEFT]:
            self.vx = -5
        if keystate[pg.K_RIGHT]:
            self.vx = 5
        if self.vx != 0 and self.vy != 0:
            # self.vx /= 1.414213562
            # self.vy /= 1.414213562

            # self.vx *= .7071
            # self.vy *= .7071

            self.vx /= math.sqrt(2)
            self.vy /= math.sqrt(2)

        if self.rect.left > WIDTH:
            self.rect.right = 0

        self.rect.x += self.vx
        self.rect.y += self.vy

class Mob(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.vel = vec(MAX_SPEED, 0).rotate(random.uniform(0,360))
        self.acc = vec(0, 0)
        self.rect.center = self.pos

    def follow_mouse(self):
        mPos = pg.mouse.get_pos()
        pPos = player.rect.center
        self.acc = (pPos - self.pos).normalize()

    def update(self):
        self.follow_mouse()
        self.vel += self.acc
        if self.vel.length() > MAX_SPEED:
            self.vel.scale_to_length((MAX_SPEED))
        self.pos += self.vel
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.rect.center = self.pos


MAX_SPEED = 5
WIDTH = 1000
HEIGHT = 800
FPS = 60
TITLE = "4-way vs 8-way movement"

BLACK = (0,0,0)
WHITE = (225,225,225)
RED = (225,0,0)
GREEN = (0,225,0)
BLUE = (0,0,225)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)
mob = Mob()
all_sprites.add(mob)

running = True
while running:
    dt = clock.tick(FPS)/1000
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()