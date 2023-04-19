import pygame
import sys
import random

pygame.init()

def Liikumine_vastupaeva():
    global posX, posY, samm
    if posX <= 0:
        posX = 0
        posY += samm
    if posY <= 0:
        posY = 0
        posX -= samm
    if posX >= X - mesilane.get_rect().width:
        posX = X - mesilane.get_rect().width
        posY -= samm
    if posY >= Y - mesilane.get_rect().height:
        posY = Y - mesilane.get_rect().height
        posX += samm

def Liikumine_paripaeva():
    global posX, posY, samm
    if posX <= 0:
        posX = 0
        posY -= samm
    if posY <= 0:
        posY = 0
        posX += samm
    if posX >= X - mesilane.get_rect().width:
        posX = X - mesilane.get_rect().width
        posY += samm
    if posY >= Y - mesilane.get_rect().height:
        posY = Y - mesilane.get_rect().height
        posX -= samm

def Vasakule_ja_paremale():
    global posX, posY, samm
    posX -= samm
    if posX > X - mesilane.get_rect().width or posX < 0: 
        samm = -samm

def Ules_ja_alla():
    global posX, posY, samm
    posY -= samm
    if posY > Y - mesilane.get_rect().width or posY < 0: 
        samm = -samm

# Варианты цветов
kollane = [255, 255, 10]
punane = [255, 0, 0]
hall = [255, 200, 200]
roosa = [255, 150, 255]
roheline = [100, 255, 100]

# Размеры экрана
X = 640
Y = 480

ekraan = pygame.display.set_mode([X, Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)

kell = pygame.time.Clock()
mesilane = pygame.image.load("among2.png")
posX = X - mesilane.get_rect().width
posY = Y - mesilane.get_rect().height
lopp = False
samm = 2
suund = random.randint(-1,2)

while not lopp:
    kell.tick(60)
    events = pygame.event.get()
    for i in pygame.event.get():
        sys.exit()

    ekraan.blit(mesilane, (posX, posY))

    if suund == 1:
        Liikumine_vastupaeva()

    if suund == -1:
        Liikumine_paripaeva()

    if suund == 0:
        Vasakule_ja_paremale()

    if suund == 2:
        Ules_ja_alla()

    pygame.display.flip()
    ekraan.fill(roheline)

pygame.quit()
