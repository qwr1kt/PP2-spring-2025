import pygame 
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Clock")

leftarm = pygame.image.load("/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab7/images/leftarm.png")  # Левая рука - сек
rightarm = pygame.image.load("/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab7/images/rightarm.png")  # Правая рука (минутная стрелка)
mainclock = pygame.transform.scale(pygame.image.load("/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab7/images/clock.png"), (800, 600))  # Фон часов

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Получаем текущее время
    current_time = time.localtime()
    minute = current_time.tm_min  # Минуты
    second = current_time.tm_sec  # Секунды

    # углы поворота для стрелок:
    second_angle = -second * 6  # 360° / 60 секунд = 6° за каждую секунду

    # Минутная стрелка (плюс 10 минут)
    minute_shift = 8  # Смещение на 10 минут вперед
    minute_angle = -(minute + minute_shift) * 6 - (second / 60) * 6  # 360° / 60 минут = 6° за каждую минуту

    # Отображаем фон (изображение часов)
    screen.blit(mainclock, (0, 0))

    # Отрисовка минутной стрелки (правая рука)
    rotated_rightarm = pygame.transform.rotate(
        pygame.transform.scale(rightarm, (800, 600)), minute_angle
    )
    rightarm_rect = rotated_rightarm.get_rect(center=(400, 300))
    screen.blit(rotated_rightarm, rightarm_rect)

    # Отрисовка секундной стрелки (левая рука)
    rotated_leftarm = pygame.transform.rotate(
        pygame.transform.scale(leftarm, (40, 600)), second_angle
    )
    leftarm_rect = rotated_leftarm.get_rect(center=(400, 300))
    screen.blit(rotated_leftarm, leftarm_rect)

    # Обновляем экран
    pygame.display.flip()

    # Ограничиваем FPS до 60 кадров в секунду
    clock.tick(60)

pygame.quit()