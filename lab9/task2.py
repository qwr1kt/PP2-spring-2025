import pygame  
import sys  
import copy  
import random  
import time  

pygame.init()  

# Размер одного блока змейки/еды
scale = 15  

score = 0  
level = 0  
SPEED = 10  # Скорость змейки (кадры в секунду)

display = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("Snake Game")  
clock = pygame.time.Clock()  

background_top = (0, 0, 50)  # верх фона (для градиента)
background_bottom = (0, 0, 0)  # низ фона
snake_colour = (255, 137, 0)  # тело змейки
snake_head = (255, 247, 0)  # голова змейки
font_colour = (255, 255, 255)  # цвет текста
defeat_colour = (255, 0, 0)  # цвет текста "Game Over"


# Класс змейки
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  
        self.y = y_start  
        self.w = scale  
        self.h = scale  
        self.x_dir = 1  # начальное движение вправо
        self.y_dir = 0  
        self.history = [[self.x, self.y]]  # список сегментов тела
        self.length = 1  # начальная длина змейки

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
            color = snake_head if i == 0 else snake_colour
            pygame.draw.rect(display, color, (self.history[i][0], self.history[i][1], self.w, self.h))

    # Проверка: съел ли еду
    def check_eaten(self, food_x, food_y, food_size):
        return abs(self.history[0][0] - food_x) < food_size and abs(self.history[0][1] - food_y) < food_size

    # Проверка: пора ли увеличить уровень
    def check_level(self):
        return self.length % 5 == 0

    # Увеличить длину змейки
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    # Проверка на столкновение с собой
    def death(self):
        for i in range(self.length - 1, 0, -1):
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
        return False

    # Обновление позиции змейки
    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale


# Класс еды
class Food:
    def __init__(self):
        self.new_location()

    # Генерация новой еды
    def new_location(self):
        self.x = random.randrange(1, int(500 / scale) - 1) * scale
        self.y = random.randrange(1, int(500 / scale) - 1) * scale
        self.value = random.choice([1, 2, 3])  # вес еды (+1, +2 или +3 очка)
        self.size = scale + (self.value - 1) * 5  # размер зависит от веса
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))  # случайный цвет
        self.spawn_time = time.time()  # время появления еды (для таймера)

    # Отображение еды
    def show(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.size, self.size))

    # Проверка: еда "протухла" (исчезает через 5 сек)
    def expired(self):
        return time.time() - self.spawn_time > 5

    # Отображение таймера еды
    def show_timer(self):
        time_left = max(0, round(5 - (time.time() - self.spawn_time), 1))
        font = pygame.font.SysFont(None, 18)
        text = font.render(str(time_left), True, font_colour)
        display.blit(text, (self.x + self.size // 2 - 5, self.y - 15))


# Отображение очков
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))


# Отображение уровня
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))


# Основной игровой цикл
def gameLoop():
    global score, level, SPEED

    snake = Snake(500 / 2, 500 / 2)
    food = Food()

    while True:
        for event in pygame.event.get():
            # Выход из игры
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            # Управление змейкой
            if event.type == pygame.KEYDOWN:
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

        # Отрисовка градиентного фона
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        # Отображение всех объектов
        snake.show()
        snake.update()
        food.show()
        food.show_timer()  # отрисовка таймера еды
        show_score()
        show_level()

        # Если змейка съела еду
        if snake.check_eaten(food.x, food.y, food.size):
            score += food.value
            snake.grow()
            food.new_location()

        # Если еда "протухла"
        if food.expired():
            food.new_location()

        # Уровень повышается каждые 5 сегментов
        if snake.check_level():
            level += 1
            SPEED += 1
            snake.grow()

        # Столкновение с собой
        if snake.death():
            score = 0
            level = 0
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)
            snake.reset()
            food.new_location()

        # Перемещение змейки за границы экрана (телепортация)
        if snake.history[0][0] > 500:
            snake.history[0][0] = 0
        if snake.history[0][0] < 0:
            snake.history[0][0] = 500
        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        pygame.display.update()
        clock.tick(SPEED)  


gameLoop()