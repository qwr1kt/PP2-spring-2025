import pygame  
import sys  
import copy  
import random  
import time  

pygame.init()  

scale = 15  
score = 0       # Счёт
level = 0       # Уровень
SPEED = 10      # Скорость (кадров в секунду)

# Начальная позиция еды
food_x = 10  
food_y = 10  

# Окно
display = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("Snake Game")  
clock = pygame.time.Clock()  

# Цвета
background_top = (0, 0, 50)  
background_bottom = (0, 0, 0)  
snake_colour = (255, 137, 0)  
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  
snake_head = (255, 247, 0)  
font_colour = (255, 255, 255)  
defeat_colour = (255, 0, 0)  


# Класс змейки
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  
        self.y = y_start  
        self.w = 15  # ширина блока
        self.h = 15  # высота блока
        self.x_dir = 1  # направление по x (вправо)
        self.y_dir = 0  # направление по y (не движется)
        self.history = [[self.x, self.y]]  # список сегментов змейки
        self.length = 1  # начальная длина

    # Сброс змейки после проигрыша
    def reset(self):
        self.x = 500 / 2 - scale  
        self.y = 500 / 2 - scale  
        self.x_dir = 1  
        self.y_dir = 0  
        self.history = [[self.x, self.y]]  
        self.length = 1  

    # Отображение змейки
    def show(self):
        for i in range(self.length):
            if i == 0:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))

    # Проверка: съела ли еду
    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    # Проверка: пора ли поднять уровень
    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True

    # Увеличить длину змейки
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    # Проверка столкновения с собой
    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    # Обновление позиции змейки
    def update(self):
        # Перемещаем каждый сегмент змейки
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        # Двигаем голову
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale


# Класс еды
class Food:
    # Генерация новой позиции еды
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale

    # Отображение еды
    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))


# Отображение счёта
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))


# Отображение уровня
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))


# Главный игровой цикл
def gameLoop():
    global score
    global level
    global SPEED

    snake = Snake(500 / 2, 500 / 2)  # создаём змейку в центре
    food = Food()
    food.new_location()  # генерируем первую еду

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # выход из игры
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # выход по кнопке Q
                    pygame.quit()
                    sys.exit()
                # Управление змейкой (вверх/вниз, влево/вправо)
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1
                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0

        # Градиентный фон
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        # Отрисовка объектов
        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()

        # Если съел еду
        if snake.check_eaten():
            food.new_location()
            score += random.randint(1, 5)  # +рандомное количество очков
            snake.grow()

        # Переход на следующий уровень
        if snake.check_level():
            food.new_location()
            level += 1
            SPEED += 1  # увеличиваем скорость
            snake.grow()

        # Столкновение с собой
        if snake.death():
            score = 0
            level = 0
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)  # задержка перед перезапуском
            snake.reset()

        # Телепортация через границы экрана
        if snake.history[0][0] > 500:
            snake.history[0][0] = 0
        if snake.history[0][0] < 0:
            snake.history[0][0] = 500
        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        pygame.display.update()
        clock.tick(SPEED)  # задержка по скорости (кадры в секунду)

# Запуск игры
gameLoop()