'''from pygame import *

#Окно
win_wight = 800
win_height = 600
window = display.set_mode((win_wight, win_height))
display.set_caption('Ping-Pong')
    #цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
window.fill(BLACK)
BALL_SPEED = 5
PLATFORM_SPEED = 10

#Классы
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
#
class Ball(GameSprite):
    def __init__(self, ball_image, ball_x, ball_y, ball_speed, wight, height):
        super().__init__('ball', ball_x, ball_y, ball_speed, wight, height)
        self.direction_x = randint(0, 1) * 2 - 1 # случайное направление по x
        self.direction_y = randint(0, 1) * 2 - 1 # случайное направление по y

    def update(self):
        # Движение шарика
        self.rect.x += self.direction_x * self.speed
        self.rect.y += self.direction_y * self.speed

        # Отскок от верхней и нижней стен
        if self.rect.y < 0 or self.rect.y > WINDOW_HEIGHT - self.rect.height:
            self.direction_y *= -1

    def reset(self):
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT // 2
        self.direction_x = randint(0, 1) * 2 - 1
        self.direction_y = randint(0, 1) * 2 - 1

racket_r = Player('quadrado.png', 30, 240, 1, 50, 150)
racket_l = Player('quadrado.png', 720, 240, 1, 50, 150)
#
ball = Ball('ball.png', win_wight // 2, win_height // 2, BALL_SPEED, 50, 50)

game = True
while game:
    window.fill(BLACK)
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket_r.update_r()
    racket_r.reset()
    racket_l.update_l()
    racket_l.reset()
    #
    ball.update()
    if ball.rect.x < 0:
        print('Вы проиграли!')
        ball.reset()
    elif ball.rect.x > win_wight - ball.rect.width:
        print('Вы выиграли!')
        ball.reset()
    #
    display.update()'''
from pygame import *
from random import *
from time import *

# Размеры окна
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

# Создание окна
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('Ping-Pong')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Скорости передвижения
BALL_SPEED = 1
PLATFORM_SPEED = 1

# Создание класса для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Создание класса для шарика
class Ball(GameSprite):
    def __init__(self, ball_image, ball_x, ball_y, ball_speed, wight, height):
        super().__init__(ball_image, ball_x, ball_y, ball_speed, wight, height)
        self.direction_x = randint(0, 1) * 2 - 1 # случайное направление по x
        self.direction_y = randint(0, 1) * 2 - 1 # случайное направление по y

    def update(self):
        # Движение шарика
        self.rect.x += self.direction_x * self.speed
        self.rect.y += self.direction_y * self.speed

        # Отскок от верхней и нижней стен
        if self.rect.y < 0 or self.rect.y > WINDOW_HEIGHT - self.rect.height:
            self.direction_y *= -1

    def reset(self):
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT // 2
        self.direction_x = randint(0, 1) * 2 - 1
        self.direction_y = randint(0, 1) * 2 - 1

# Создание класса для платформы
class Platform(GameSprite):
    def update(self):
        # Движение платформы
        keys = key.get_pressed()
        if keys[self.key_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.key_down] and self.rect.y < WINDOW_HEIGHT - self.rect.height:
            self.rect.y += self.speed

# Создание объектов
ball = Ball('ball.png', WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_SPEED, 50, 50)
platform_left = Platform('quadrado.png', 50, WINDOW_HEIGHT // 2 - 50, PLATFORM_SPEED, 20, 170)
platform_left.key_up = K_w
platform_left.key_down = K_s
platform_right = Platform('quadrado.png', WINDOW_WIDTH - 70, WINDOW_HEIGHT // 2 - 50, PLATFORM_SPEED, 20, 170)
platform_right.key_up = K_UP
platform_right.key_down = K_DOWN

# Группы спрайтов
all_sprites = sprite.Group()
all_sprites.add(ball, platform_left, platform_right)

#текст
font.init()
font = font.Font(None, 70)
win = font.render('1-ый ИГРОК ВЫЙГРАЛ!', True, (0, 255, 0))
lose = font.render('2-ой ИГРОК ВЫЙГРАЛ!', True, (255, 0, 0))

# Основной цикл программы
finish = False
game_over = False
game = True
while game:
    # Обработка событий
    for j in event.get():
        if j.type == QUIT:
            game = False
    if finish != True:
        # Обновление спрайтов
        ball.update()
        platform_left.update()
        platform_right.update()

        # Проверка столкновения шарика с платформами
        if sprite.collide_rect(ball, platform_left) or sprite.collide_rect(ball, platform_right):
            ball.direction_x *= -1

        # Отрисовка спрайтов
        window.fill(BLACK)
        all_sprites.draw(window)

        # Проверка проигрыша и победы
        if ball.rect.x < 0:
            finish = True
            sleep(1.5)
            window.blit(lose, (200, 200))
            game_over = True
        elif ball.rect.x > WINDOW_WIDTH - ball.rect.width:
            finish = True
            window.blit(win, (200, 200))
            game_over = True
            

        # Обновление экрана
        display.update()