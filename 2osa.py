import pygame

pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill(( 0, 0, 0))
pygame.display.set_caption("Lumememm - Artemi Mihhalenkov")


lil=pygame.Rect(130,10,50,50)
pygame.draw.ellipse(ekraani_pind, (250,250,250), lil)

lil=pygame.Rect(140,25,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,200), lil)

lil=pygame.Rect(163,25,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,200), lil)

lil=pygame.Rect(151,38,7,12)
pygame.draw.ellipse(ekraani_pind, (255,165,0), lil)

lil=pygame.Rect(123,58,65,65)
pygame.draw.ellipse(ekraani_pind, (250,250,250), lil)

lil=pygame.Rect(152,70,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,0), lil)

lil=pygame.Rect(152,90,7,7)
pygame.draw.ellipse(ekraani_pind, (0,0,0), lil)

lil=pygame.Rect(113,120,85,85)
pygame.draw.ellipse(ekraani_pind, (250,250,250), lil)



pygame.display.flip()

while True:
    event=pygame.event.poll()  
    if event.type==pygame.QUIT:
        break

pygame.quit() 


