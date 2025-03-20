import pygame
import os

pygame.init()

playlist = []  
music_folder = "/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab7/graduation"
allmusic = os.listdir(music_folder)  

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

screen = pygame.display.set_mode((int(2500*0.5) , int(1407*0.5)))  
pygame.display.set_caption("Music Player")  
clock = pygame.time.Clock() 

background = pygame.image.load(os.path.join("music-elements", "background.png"))
background = pygame.transform.scale(background, (int(2500*0.5) , int(1407*0.5)))  

#текущий трек 
font2 = pygame.font.SysFont("Roboto", 30, bold=True)

# изображения кнопок
playb = pygame.image.load(os.path.join("music-elements", "play.png")).convert_alpha()
pausb = pygame.image.load(os.path.join("music-elements", "pause.png")).convert_alpha()
nextb = pygame.image.load(os.path.join("music-elements", "next.png")).convert_alpha()
prevb = pygame.image.load(os.path.join("music-elements", "back.png")).convert_alpha()

# индекс для номера песни
index = 0  
pygame.mixer.music.load(playlist[index])  
pygame.mixer.music.play(1)  
aplay = True 

run = True 
while run:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  
            pygame.quit() 
            exit()  
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE:  
                if aplay: 
                    aplay = False  
                    pygame.mixer.music.pause()
                else:  
                    aplay = True  
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:  
                index = (index + 1) % len(playlist) 
                pygame.mixer.music.load(playlist[index])  
                pygame.mixer.music.play()  

            if event.key == pygame.K_LEFT:  
                index = (index - 1) % len(playlist)  
                pygame.mixer.music.load(playlist[index])  
                pygame.mixer.music.play() 

        # управление мышкой 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        playb_rect = playb.get_rect(topleft=(2500*0.23 - 10, 1407*0.19))
        pausb_rect = pausb.get_rect(topleft=(2500*0.23 - 10, 1407*0.19))
        nextb_rect = nextb.get_rect(topleft=(2500*0.23 + 200, 1407*0.19 + 8))
        prevb_rect = prevb.get_rect(topleft=(2500*0.23 - 200, 1407*0.19 + 8))

        playb_rect = playb_rect.inflate(20, 20)
        pausb_rect = pausb_rect.inflate(20, 20)
        nextb_rect = nextb_rect.inflate(20, 20)
        prevb_rect = prevb_rect.inflate(20, 20)

        if playb_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
            if aplay:
                aplay = False
                pygame.mixer.music.pause()
            else:
                aplay = True
                pygame.mixer.music.unpause()

        if nextb_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
            index = (index + 1) % len(playlist)
            pygame.mixer.music.load(playlist[index])
            pygame.mixer.music.play()

        if prevb_rect.collidepoint(mouse_x, mouse_y) and mouse_click[0]:
            index = (index - 1) % len(playlist)
            pygame.mixer.music.load(playlist[index])
            pygame.mixer.music.play()

       
    text2 = font2.render(os.path.basename(playlist[index]), True, (225, 225, 225))

    screen.blit(background, (0, 0))  
    screen.blit(text2, (2500*0.23-96, 108))

    #кнопки
    playb = pygame.transform.scale(playb, (123, 123))  
    pausb = pygame.transform.scale(pausb, (123, 123))  

    if aplay:
        screen.blit(pausb, (2500*0.23-10, 1407*0.19))
    else: 
        screen.blit(playb, (2500*0.23-10, 1407*0.19))
    
    nextb = pygame.transform.scale(nextb, (100, 100))  
    screen.blit(nextb, (2500*0.23 + 200, 1407*0.19+8))  
    
    prevb = pygame.transform.scale(prevb, (100, 100))  
    screen.blit(prevb, (2500*0.23 - 200, 1407*0.19+8)) 

    clock.tick(60)
    pygame.display.update() 