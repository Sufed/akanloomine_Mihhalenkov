import pygame,sys
pygame.init()
#värvid
kollane=[255,255,10]
punane=[255,0,0]
hall=[255,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("among2.png")
posX=X-mesilane.get_rect().width
posY=Y-mesilane.get_rect().height
lõpp=False
samm=2
while not lõpp:
    kell.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT():
            sys.exit()
    ekraan.blit(mesilane,(posX,posY))

    if posX <= 0:
        posX = 0
        posY -= samm

    if posY <= 0:
        posY = 0
        posX += samm + 2


    if posX >= X - mesilane.get_rect().width:
        posX = X - mesilane.get_rect().width
        posY += samm

    if posY >= Y - mesilane.get_rect().height:
        posY = Y - mesilane.get_rect().height
        posX -= samm + 2

    pygame.display.flip()
    ekraan.fill(roheline)
pygame.quit()
