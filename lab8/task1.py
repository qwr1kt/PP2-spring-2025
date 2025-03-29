import pygame, sys
from pygame.locals import *
import random, time
import os

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3 # скорость движения врагов и фона
SCORE = 0 # счёт за объезд врагов
COINS = 0 # общее количество монет

font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(os.path.join("lab8", "AnimatedStreet.png"))

screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("lab8", "Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1  # увеличиваем счёт за каждого объезженного врага
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Флаги для увеличения скорости (накапливаются по достижению определённого количества монет)
c1, c2, c3, c4, c5 = False, False, False, False, False

# Класс монетки
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("lab8", "coin.png"))
        self.image = pygame.transform.scale(self.image, (40, 40))  # размер монеты
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40),
                            random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        global COINS, SPEED
        coin_value = random.randint(1, 3)  # монета может дать от 1 до 3 очков
        COINS += coin_value

        # увеличение скорости игры по мере сбора монет
        global c1, c2, c3, c4, c5
        if not c1 and COINS >= 10:
            SPEED += 1
            c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1
            c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1
            c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1
            c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1
            c5 = True

        # монета появляется в новой случайной позиции
        self.rect.top = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40),
                            random.randint(40, SCREEN_HEIGHT - 40))

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("lab8", "Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # стартовая позиция

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

# Создание экземпляров классов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coinss = pygame.sprite.Group()
coinss.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Событие для автоматического увеличения скорости со временем
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # каждые 1000 мс (1 сек)

# Экран окончания игры
def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return True
                elif event.key == K_ESCAPE:
                    return False

# Обработка столкновения с врагом
def handle_crash():
    screen.fill(RED)
    screen.blit(game_over, (120, 250))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return True
                elif event.key == K_ESCAPE:
                    return False

# Сброс игры
def restart_game():
    global SCORE, COINS, SPEED, c1, c2, c3, c4, c5
    global P1, C1, E1
    SCORE = 0
    COINS = 0
    SPEED = 3
    c1, c2, c3, c4, c5 = False, False, False, False, False

    # сброс таймера
    pygame.time.set_timer(INC_SPEED, 0)
    pygame.time.set_timer(INC_SPEED, 1000)

    # очистка всех спрайтов
    enemies.empty()
    coinss.empty()
    all_sprites.empty()

    # пересоздание объектов
    P1 = Player()
    E1 = Enemy()
    C1 = Coin()
    enemies.add(E1)
    coinss.add(C1)
    all_sprites.add(P1, E1, C1)

# Начальная позиция фона
background_y = 0

#Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1  # плавное ускорение с течением времени
        if event.type == QUIT:
            pygame.quit(); sys.exit()

    # Столкновение игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        if not handle_crash():
            pygame.quit(); sys.exit()
        else:
            restart_game()
            continue

    # Движение фона вниз
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Отображение счёта и количества монет
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Отрисовка всех объектов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if entity == C1 and pygame.sprite.spritecollideany(P1, coinss):
            entity.move()
        else:
            entity.move()

    # Движение монетки вниз
    for coin in coinss:
        coin.rect.y += SPEED
        if coin.rect.top > SCREEN_HEIGHT:
            # если ушла за нижнюю границу — респавн наверху
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    # Обновление экрана
    pygame.display.update()
    FramePerSec.tick(FPS)