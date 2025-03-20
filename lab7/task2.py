import pygame
import os

pygame.init()

playlist = []  
music_folder = "/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab7/graduation"
allmusic = os.listdir(music_folder)  

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

screen = pygame.display.set_mode((2500*0.5 , 1407*0.5))  # Устанавливаем размер окна
pygame.display.set_caption("Music Player")  # Устанавливаем заголовок окна
clock = pygame.time.Clock() 

background = pygame.image.load(os.path.join("music-elements", "background.png"))
background = pygame.transform.scale(background, (2500*0.5 , 1407*0.5))  # Изменяем размер фона

# Создаем фон для кнопок, с размерами и белым цветом
bg = pygame.Surface((500, 200), pygame.SRCALPHA)
# Шрифт для отображения названия текущей песни
font2 = pygame.font.SysFont(None, 20)

# Загружаем изображения кнопок
playb = pygame.image.load(os.path.join("music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))

index = 0  # Индекс текущей песни в плейлисте
aplay = False  # Флаг, указывающий, проигрывается ли музыка в данный момент

# Загружаем и начинаем воспроизведение первой песни из плейлиста
pygame.mixer.music.load(playlist[index])  
pygame.mixer.music.play(1)  # Воспроизводим один раз
aplay = True  # Устанавливаем флаг, что музыка играет

run = True  # Основной цикл программы
while run:
    for event in pygame.event.get():  # Обрабатываем события
        if event.type == pygame.QUIT:  # Если окно закрыто
            run = False  # Прерываем цикл
            pygame.quit()  # Завершаем Pygame
            exit()  # Выходим из программы
        elif event.type == pygame.KEYDOWN:  # Если нажата клавиша
            if event.key == pygame.K_SPACE:  # Если нажали пробел
                if aplay:  # Если музыка играет
                    aplay = False  # Ставим флаг в False, приостанавливаем музыку
                    pygame.mixer.music.pause()
                else:  # Если музыка приостановлена
                    aplay = True  # Возобновляем воспроизведение
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:  # Если нажали стрелку вправо
                index = (index + 1) % len(playlist)  # Переходим к следующей песне в плейлисте
                pygame.mixer.music.load(playlist[index])  # Загружаем новую песню
                pygame.mixer.music.play()  # Начинаем воспроизведение

            if event.key == pygame.K_LEFT:  # Если нажали стрелку влево
                index = (index - 1) % len(playlist)  # Переходим к предыдущей песне в плейлисте
                pygame.mixer.music.load(playlist[index])  # Загружаем новую песню
                pygame.mixer.music.play()  # Начинаем воспроизведение

        # Проверка на нажатие кнопок (play/pause, next, prev)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if playb.get_rect(topleft=(370, 590)).collidepoint(mouse_x, mouse_y) and mouse_click[0]:
            if aplay:  # Если музыка играет
                aplay = False
                pygame.mixer.music.pause()
            else:  # Если музыка на паузе
                aplay = True
                pygame.mixer.music.unpause()

        if nextb.get_rect(topleft=(460, 587)).collidepoint(mouse_x, mouse_y) and mouse_click[0]:
            index = (index + 1) % len(playlist)
            pygame.mixer.music.load(playlist[index])
            pygame.mixer.music.play()

        if prevb.get_rect(topleft=(273, 585)).collidepoint(mouse_x, mouse_y) and mouse_click[0]:
            index = (index - 1) % len(playlist)
            pygame.mixer.music.load(playlist[index])
            pygame.mixer.music.play()

    # Отображаем название текущей песни на экране
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    
    # Отображаем фоновое изображение и другие элементы на экране
    screen.blit(background, (0, 0))  # Фон
    screen.blit(bg, (155, 500))  # Фон для кнопок
    screen.blit(text2, (365, 520))  # Название текущей песни

    # Масштабируем кнопки
    playb = pygame.transform.scale(playb, (70, 70))  # Масштабируем кнопку "Play"
    pausb = pygame.transform.scale(pausb, (70, 70))  # Масштабируем кнопку "Pause"
    
    # Если музыка играет, показываем кнопку паузы, иначе кнопку воспроизведения
    if aplay:
        screen.blit(pausb, (370, 590))
    else: 
        screen.blit(playb, (370, 590))
    
    nextb = pygame.transform.scale(nextb, (70, 70))  # Масштабируем кнопку "Next"
    screen.blit(nextb, (460, 587))  # Размещаем кнопку "Next"
    
    prevb = pygame.transform.scale(prevb, (75, 75))  # Масштабируем кнопку "Prev"
    screen.blit(prevb, (273, 585))  # Размещаем кнопку "Prev"



    clock.tick(24)  # Обновляем экран 24 раза в секунду
    pygame.display.update()  # Обновляем отображение на экране 