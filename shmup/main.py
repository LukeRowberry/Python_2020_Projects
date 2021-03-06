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
        self.shield = 100
        # self.image = pg.Surface((50,40))
        # self.image.fill(PURPLE)
        self.image = player_img
        self.image = pg.transform.scale(player_img,(50,40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH/2)
        self.rect.centery = (HEIGHT - (HEIGHT*.05))
        self.speedx = 0
        self.shoot_delay = 350
        self.last_shot = pg.time.get_ticks()
        self.lives = 3
        self.hide_timer = pg.time.get_ticks()
        self.hidden = False
        self.power_level = 1
        self.pow_timer = pg.time.get_ticks()

    def shield_up(self,num):
        self.shield += num
        if self.shield >= 100:
            self.shield = 100

    def gun_pow(self):
        self.power_level += 1
        self.pow_timer = pg.time.get_ticks()

    def hide(self):
        self.lives -= 1
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.last_shot >= self.shoot_delay:
            self.last_shot = now
            if self.power_level == 1:
                b = Bullet(self.rect.centerx,self.rect.top + 1)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_sound.play()
            elif self.power_level == 2:
                b1 = Bullet(self.rect.left, self.rect.centery + 1)
                b2 = Bullet(self.rect.right, self.rect.centery + 1)
                all_sprites.add(b1,b2)
                bullet_group.add(b1,b2)
                shoot_sound.play()
            elif self.power_level == 3:
                b1 = Bullet(self.rect.left, self.rect.centery + 1)
                b1.spread_up(-3)
                b2 = Bullet(self.rect.centerx,self.rect.top + 1)
                b3 = Bullet(self.rect.right, self.rect.centery + 1)
                b3.spread_up(3)
                all_sprites.add(b1, b2, b3)
                bullet_group.add(b1, b2, b3)
                shoot_sound.play()

    def update(self):
        if self.power_level >= 2 and pg.time.get_ticks() - self.pow_timer > POWERUP_TIME:
            self.power_level -= 1
            self.pow_timer = pg.time.get_ticks()

        if self.hidden and pg.time.get_ticks() - self.hide_timer > 3000:
            self.hidden = False
            self.rect.centery = (HEIGHT - (HEIGHT*.05))
            self.rect.centerx = (WIDTH / 2)
            self.shield = 100

        self.rect.x += self.speedx
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate[pg.K_SPACE] and not self.hidden:
            player.shoot()
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
        self.spread = 0

    def spread_up(self,num):
        self.spread = num

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.spread
        if self.rect.bottom < 0:
            self.kill()

class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        # self.image = pg.Surface((25,25))
        # self.image.fill(RED)
        self.image_original = r.choice(meteor_images)
        self.image_original.set_colorkey(BLACK)
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.75/2)
        #pg.draw.circle(self.image, RED, self.rect.center,self.radius)
        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = r.randrange(-100, -40)
        self.speedy = r.randrange(1, 8)
        self.speedx = r.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = r.randint(-8,8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            #Doing rotation
            self.rot = (self.rot + self.rot_speed)%360
            new_image = pg.transform.rotate(self.image_original, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def spawn(self):
        npc = Npc()
        npc_group.add(npc)
        all_sprites.add(npc)

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = r.randrange(WIDTH - self.rect.width)
            self.rect.y = r.randrange(-100, -40)
            self.speedy = r.randrange(1, 8)

class Explosion(pg.sprite.Sprite):
    def __init__(self,center,size):
        super(Explosion, self).__init__()
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_rate = 50
        self.last_update = pg.time.get_ticks()


    def update(self):
        now = pg.time.get_ticks()
        if now-self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Pow(pg.sprite.Sprite):
    def __init__(self,center):
        super(Pow, self).__init__()
        self.type = r.choice(powerups_chance)
        self.image = pows_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

########################################################################



#Game Function
########################################################################
def draw_text(surf,text,size,x,y,color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)
def draw_bar(surf,x,y,pct):
    if pct < 0:
        pct = 0
    bar_length = 180
    bar_height = 25
    fill = (pct/100)*bar_length
    outline_rect = pg.Rect(x,y,bar_length,bar_height)
    fill_rect = pg.Rect(x,y,fill,bar_height)
    pg.draw.rect(surf,GREEN,fill_rect)
    pg.draw.rect(surf,WHITE,outline_rect,3)
    if player.shield <= 67 and player.shield > 34:
        pg.draw.rect(surf, YELLOW, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 3)
    if player.shield <= 34:
        pg.draw.rect(surf, RED, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 3)
def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x+40 * i
        img_rect.y = y
        surf.blit(img,img_rect)
def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "SHMUP!",64, WIDTH/2, HEIGHT/4,WHITE)
    draw_text(screen, "Use the ARROW keys or WASD keys to move",22,WIDTH/2,HEIGHT/2,WHITE)
    draw_text(screen, "Use the SPACEBAR to fire", 22, WIDTH / 2, (HEIGHT/2)-30, WHITE)
    draw_text(screen, "Press any key to begin",18, WIDTH/2, HEIGHT*3/4,WHITE)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False
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
font_name = pg.font.match_font("arial")
powerups_list = ["gun","shield"]
powerups_chance = ["gun","gun","shield","shield","shield","shield","shield","shield","shield","shield"]
POWERUP_TIME = 10000
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
animation_folder = path.join(images_folder,"animations")
player_animation_folder = path.join(animation_folder,"player_animation")
npc_animation_folder = path.join(animation_folder,"npc_animation")
pow_folder = path.join(images_folder,"powerups")
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
player_mini_img = pg.transform.scale(player_img,(33,26))
player_mini_img.set_colorkey(BLACK)

#Asteroid
npc_image = pg.image.load(path.join(enemy_img_folder,"meteor.png")).convert()
meteor_images = []
meteor_list = ['meteorBrown_big1.png',
               'meteorBrown_big2.png',
               'meteorBrown_big3.png',
               'meteorBrown_big4.png',
               'meteorBrown_med1.png',
               'meteorBrown_med3.png',
               'meteorBrown_small1.png',
               'meteorBrown_small2.png',
               'meteorBrown_tiny1.png',
               'meteorBrown_tiny2.png',
               'meteorGrey_big1.png',
               'meteorGrey_big2.png',
               'meteorGrey_big3.png',
               'meteorGrey_big4.png',
               'meteorGrey_med1.png',
               'meteorGrey_med2.png',
               'meteorGrey_small1.png',
               'meteorGrey_small2.png',
               'meteorGrey_tiny1.png',
               'meteorGrey_tiny2.png']
for image in meteor_list:
    meteor_images.append(pg.image.load(path.join(enemy_img_folder,image)))
#Laser
laser_img = pg.image.load(path.join(player_img_folder,"laser.png")).convert()
#Animations
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
explosion_anim["player"] = []
for i in range(0,9):
    fn = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(npc_animation_folder,fn)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img, (100, 100))
    img_sm = pg.transform.scale(img, (40, 40))
    explosion_anim["lg"].append(img_lg)
    explosion_anim["sm"].append(img_sm)
    #Adding Player Animations
    fn = "sonicExplosion0{}.png".format(i)
    img = pg.image.load(path.join(player_animation_folder, fn)).convert()
    img.set_colorkey(BLACK)
    explosion_anim["player"].append(img)
#Powerups
pows_images = {}
for i in range(len(powerups_list)):
    fn = "pow_img_{}.png".format(i)
    pows_images[powerups_list[i]] = pg.image.load(path.join(pow_folder,fn)).convert()
########################################################################



#Load Sounds
########################################################################
shoot_sound = pg.mixer.Sound(path.join(sounds_folder,"pew.wav"))
explosion_sounds = []
for sound in ['expl3.wav','expl6.wav']:
    explosion_sounds.append(pg.mixer.Sound(path.join(sounds_folder, sound)))
pg.mixer.music.load(path.join(sounds_folder,"tgfcoder-FrozenJam-SeamlessLoop.ogg"))
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(loops=-1)
########################################################################



#Game Loop
########################################################################

#Game Update Variables
###########################################################
playing = True
game_over = True
score = 0
###########################################################
###########################################################
while playing:
    if game_over:
        show_go_screen()
        game_over = False
        # Sprite Groups
        ###########################################
        all_sprites = pg.sprite.Group()
        players_group = pg.sprite.Group()
        npc_group = pg.sprite.Group()
        bullet_group = pg.sprite.Group()
        pows_group = pg.sprite.Group()
        ###########################################

        #Create Game Objects
        ###########################################
        player = Player()

        for i in range(10):
            npc = Npc()
            npc_group.add(npc)
        ###########################################

        #Add Objects to Sprite Groups
        ###########################################
        players_group.add(player)

        for i in players_group:
            all_sprites.add(i)
        for i in npc_group:
            all_sprites.add(i)
        ###########################################

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
            if event.key == pg.K_ESCAPE:
                playing = False
    ###########################################

    #Updates
    ###########################################

    all_sprites.update()
    #Npc hits player
    hits = pg.sprite.spritecollide(player,npc_group,True,pg.sprite.collide_circle)
    for hit in hits:
        npc.spawn()
        r.choice(explosion_sounds).play()
        player.shield -= hit.radius*2
        expl = Explosion(hit.rect.center, "sm")
        all_sprites.add(expl)
        if player.shield <= 0:
            death_expl = Explosion(player.rect.center,"player")
            all_sprites.add(death_expl)
            player.hide()
            if player.lives <= 0:  #and not death_expl.alive(): --needs fix
                game_over = True
    #Bullet hits Npc
    hits = pg.sprite.groupcollide(npc_group,bullet_group, True, True)
    for hit in hits:
        score += 50 - hit.radius
        expl = Explosion(hit.rect.center,"lg")
        all_sprites.add(expl)
        npc.spawn()
        r.choice(explosion_sounds).play()
        if r.random() > .90:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            pows_group.add(pow)
      #Powerup hits player
    hits = pg.sprite.spritecollide(player, pows_group, True, pg.sprite.collide_circle)
    for hit in hits:
        if hit.type == "shield":
            num = r.randint(15,30)
            player.shield_up(num)
        elif hit.type == "gun":
            player.gun_pow()
    ###########################################

    #Render/Draw
    ###########################################
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    #Draw hud
    draw_text(screen,"Score: "+str(score),25,WIDTH/2,10,WHITE)
    draw_bar(screen, 5, 10, player.shield)
    draw_lives(screen, 30, 50, player.lives, player_mini_img)
    pg.display.flip()
    ###########################################
###########################################################
###########################################################
pg.quit()
########################################################################