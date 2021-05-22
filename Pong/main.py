import pygame as pg, sys, random


class Block(pg.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pg.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

class Player(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constrain()

class Ball(Block):
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles):
        super().__init__(path, x_pos, y_pos)
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.paddles = paddles
        self.active = False
        self.score_time = 0

    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()

    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            pg.mixer.Sound.play(plob_sound)
            self.speed_y *= -1

        if pg.sprite.spritecollide(self, self.paddles, False):
            pg.mixer.Sound.play(plob_sound)
            collision_paddle = pg.sprite.spritecollide(self, self.paddles, False)[0].rect
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1

    def reset_ball(self):
        self.active = False
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        self.score_time = pg.time.get_ticks()
        self.rect.center = (screen_width / 2, screen_height / 2)
        pg.mixer.Sound.play(score_sound)

    def restart_counter(self):
        current_time = pg.time.get_ticks()
        countdown_number = 3

        if current_time - self.score_time <= 700:
            countdown_number = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown_number = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown_number = 1
        if current_time - self.score_time >= 2100:
            self.active = True

        time_counter = basic_font.render(str(countdown_number), True, accent_color)
        time_counter_rect = time_counter.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
        pg.draw.rect(screen, bg_color, time_counter_rect)
        screen.blit(time_counter, time_counter_rect)

class Opponent(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed

    def update(self, ball_group):
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed
        self.constrain()

    def constrain(self):
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= screen_height: self.rect.bottom = screen_height

class GameManager():
    def __init__(self, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        #Drawing Game Objects
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        #Updating Game Objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= screen_width:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = basic_font.render(str(self.player_score), True, accent_color)
        opponent_score = basic_font.render(str(self.opponent_score), True, accent_color)

        player_score_rect = player_score.get_rect(midleft=(screen_width / 2 + 40, screen_height / 2))
        opponent_score_rect = opponent_score.get_rect(midright=(screen_width / 2 - 40, screen_height / 2))

        screen.blit(player_score, player_score_rect)
        screen.blit(opponent_score, opponent_score_rect)

#General Setup
pg.mixer.pre_init(44100, -16, 2, buffer = 512)
pg.init()
clock = pg.time.Clock()

#Settings
screen_width = 1280
screen_height = 960
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Pong")

#Global Variables
bg_color = pg.Color("#2F373F")
accent_color = (27, 35, 43)
basic_font = pg.font.Font("freesansbold.ttf", 32)
plob_sound = pg.mixer.Sound("pong.ogg")
score_sound = pg.mixer.Sound("score.ogg")
middle_strip = pg.Rect(screen_width/2 - 2, 0, 4, screen_height)

#Game Objects
player = Player("Paddle.png", screen_width - 20, screen_height / 2, 5)
opponent = Opponent("Paddle.png", 20, screen_width / 2, 50)
paddle_group = pg.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball_image = pg.image.load('Ball.png')
ball = Ball("Ball.png", screen_width / 2, screen_height / 2, 4, 4, paddle_group)
ball_sprite = pg.sprite.GroupSingle()
ball_sprite.add(ball)

pg.display.set_icon(ball_image)
game_manager = GameManager(ball_sprite, paddle_group)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.movement -= player.speed
            if event.key == pg.K_DOWN:
                player.movement += player.speed
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                player.movement += player.speed
            if event.key == pg.K_DOWN:
                player.movement -= player.speed

    #Background
    screen.fill(bg_color)
    pg.draw.rect(screen, accent_color, middle_strip)

    #Run Game
    game_manager.run_game()

    #Rendering
    pg.display.flip()
    clock.tick(120)