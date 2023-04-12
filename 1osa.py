import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("Esimene aken")

ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0,255,0),ristkülik)
jalg=pygame.Rect(310,180,30,200)
pygame.draw.rect(ekraani_pind,(50,205,0),jalg)
lill=pygame.Rect(200,100,250,200)
pygame.draw.ellipse(ekraani_pind,(255,255,0),lill)

pilt=pygame.image.load("among1.png")
ekraani_pind.blit(pilt,(300,50))

font=pygame.font.SysFont("Broadway",40)
sõnad="Tere tulemast!"
varv=[200,200,200]
teksti_lisamine=font.render(sõnad,False,varv)
ekraani_pind.blit(teksti_lisamine,(150,25))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
