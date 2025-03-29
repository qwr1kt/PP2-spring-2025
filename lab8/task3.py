import pygame

# 🎨 Управление:
# P - Кисть (pen)
# R - Прямоугольник
# C - Круг
# E - Ластик
# 1–5 - Цвета (чёрный, зелёный, красный, синий, жёлтый)
# Q - Очистить экран

WIDTH, HEIGHT = 1200, 800
FPS = 60
draw = False
radius = 5
color = 'blue'
mode = 'pen'

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mini Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
font = pygame.font.SysFont(None, 60)

# Рисуем прямоугольник
def drawRectangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    rect = pygame.Rect(min(x1, x2), min(y1, y2), widthr, height)
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

# Рисуем круг
def drawCircle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    radius = abs(x1 - x2) // 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)

# Рисуем кистью (линия между точками)
def drawLine(screen, start, end, width, color):
    pygame.draw.line(screen, pygame.Color(color), start, end, width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Горячие клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: mode = 'pen'
            if event.key == pygame.K_r: mode = 'rectangle'
            if event.key == pygame.K_c: mode = 'circle'
            if event.key == pygame.K_e: mode = 'erase'
            if event.key == pygame.K_q: screen.fill(pygame.Color('white'))

            if event.key == pygame.K_1: color = 'black'
            if event.key == pygame.K_2: color = 'green'
            if event.key == pygame.K_3: color = 'red'
            if event.key == pygame.K_4: color = 'blue'
            if event.key == pygame.K_5: color = 'yellow'

        # Нажатие мыши — начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            if mode in ['pen', 'erase']:
                pygame.draw.circle(screen, pygame.Color('white' if mode == 'erase' else color), event.pos, radius)
            prevPos = event.pos

        # Отпускание мыши — рисуем фигуру
        if event.type == pygame.MOUSEBUTTONUP:
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            draw = False

        # Движение мыши — рисуем (кисть или ластик)
        if event.type == pygame.MOUSEMOTION:
            if draw and mode in ['pen', 'erase']:
                drawLine(screen, prevPos, event.pos, radius, 'white' if mode == 'erase' else color)
                prevPos = event.pos

    # Отображение текущего радиуса и цвета
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = font.render(str(radius), True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))

    pygame.display.flip()
    clock.tick(FPS)