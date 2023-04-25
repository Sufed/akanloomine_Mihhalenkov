import pygame
import sys
import random

pygame.init()

X = 640
Y = 480

Valge = (255, 255, 255)
Must = (0, 0, 0)
Kollane = (255, 255, 0)

Õuna_suurus = 20
Korvi_laius = 30
Korvi_kõrgus = 30

Õun_X = random.randint(0, X - Õuna_suurus)
Õun_Y = 0

Korvi_X = X // 2 - Korvi_laius // 2
Korvi_Y = Y // 1.5

Õuna_kiirus = 5

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Õuna ja korviga mängimine")

õuna_pilt = pygame.image.load("õun.png")  # для яблока
korvi_pilt = pygame.image.load("among2.png")  # для корзины

clock = pygame.time.Clock()
#score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Õun_Y += Õuna_kiirus

    #if Õun_Y >= Y:
    #    score -= 1
    #    Õun_X = random.randint(0, X - Õuna_suurus)
    #    Õun_Y = 0

    #if Õun_Y + Õuna_suurus >= Korvi_Y and Õun_X + Õuna_suurus >= Korvi_X and Õun_X <= Korvi_X + Korvi_laius:
    #    score += 1
    #    Õun_X = random.randint(0, X - Õuna_suurus)
    #    Õun_Y = 0

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT] and Korvi_X > 0:
    #    Korvi_X -= 5
    #if keys[pygame.K_RIGHT] and Korvi_X < X - Korvi_laius:
    #    Korvi_X += 5

    screen.fill(Valge)

    #for enemy in enemies[:]:
    #    if player.colliderect(enemy):
    #        enemies.remove(enemy)
    #        score += 1

    screen.blit(õuna_pilt, (Õun_X, Õun_Y)) # Отображение изображения яблока на экране
    screen.blit(korvi_pilt, (Korvi_X, Korvi_Y)) # Отображение изображения корзины на экране

    #font = pygame.font.Font(None, 36)
    #score_text = font.render("Счет: {}".format(score), True, Must)
    #screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

















#import pygame, random
#import pygame, random
 
##sounds = ['snd1.mp3', 'snd2.mp3', 'snd3.mp3', 'snd4.mp3', 'snd5.mp3']
##pygame.mixer.music.load('music/'+random.choice(sounds))
##pygame.mixer.music.play()

##pygame.mixer.music.set_volume(0.2)

##hit_sound = pygame.mixer.Sound('music/Hit.wav')
##pygame.mixer.Sound.play(hit_sound)

#pygame.init()

#red = [255, 0, 0]
#green = [0, 255, 0]
#blue = [0, 0, 255]
#pink = [255, 153, 255]
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]

#screenX = 640
#screenY = 480
#screen=pygame.display.set_mode([screenX,screenY])
#pygame.display.set_caption("Surface")
#screen.fill(lBlue)
#clock = pygame.time.Clock()
#posX, posY = 0, 0
#speedX, speedY = 3, 4

#player = pygame.Rect(posX, posY, 120, 120)
#playerImage = pygame.image.load("among2.png")
#playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

#enemies = []
#for i in range(5):
#    enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0,screenY - 100), 60, 73))
#enemyImage = pygame.image.load("õun.png")
#enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])

#enemyCounter = 0
#totalEnemies = 20
#score = 0

#gameover = False
#while not gameover:
#    clock.tick(60)

#    event = pygame.event.poll()
#    if event.type == pygame.QUIT:
#        break
#    player = pygame.Rect(posX, posY, 120, 140)
#    screen.blit(playerImage,player)

#    posX += speedX
#    posY += speedY

#    if posX > screenX-playerImage.get_rect().width or posX <0:
#        speedX = -speedX

#    if posY > screenY-playerImage.get_rect().width or posY <0:
#        speedY = -speedY
#    enemyCounter += 1
#    if enemyCounter >= totalEnemies:
#        enemyCounter = 0
#        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))

#    for enemy in enemies[:]:
#        if player.colliderect(enemy):
#            enemies.remove(enemy)
#            score += 1

#    for enemy in enemies:
#        screen.blit(enemyImage, enemy)

#    pygame.display.flip()
#    screen.fill(blue)

#    print(score)
#    if score == 20:
#        gameover = True
#pygame.quit()
