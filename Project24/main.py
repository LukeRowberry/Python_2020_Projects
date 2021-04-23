import pygame as pg
import math

class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Player, self).__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, dt):
        self.vx,self.vy = 200*dt,0
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
player = Player(WIDTH/2, HEIGHT/2)
all_sprites.add(player)

running = True
while running:
    dt = clock.tick(FPS)/1000
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    all_sprites.update(dt)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()