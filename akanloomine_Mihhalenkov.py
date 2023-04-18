
import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0, 191, 255))
pygame.display.set_caption("Esimene aken")

ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0, 255, 0),ristkülik)

jalg=pygame.Rect(190,200,30,200)
pygame.draw.rect(ekraani_pind,(139, 69, 19),jalg)

ristkülik=pygame.Rect(150,200,110,130)
pygame.draw.rect(ekraani_pind,(0, 128, 0),ristkülik)


jalg=pygame.Rect(490,200,30,200)
pygame.draw.rect(ekraani_pind,(139, 69, 19),jalg)

ristkülik=pygame.Rect(450,200,110,130)
pygame.draw.rect(ekraani_pind,(0, 128, 0),ristkülik)

pilt=pygame.image.load("among2.png")
ekraani_pind.blit(pilt,(330,290))

font=pygame.font.SysFont("Alganian",40)
sõnad="Где я?"
värv=[0, 0, 0]
teksti_lisanime=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisanime,(330,250))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
