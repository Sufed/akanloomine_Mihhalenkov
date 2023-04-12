import pygame
import random
import sys

def Maja(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y- ((3/4.0) * kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0) * kõrgus), (x,y-((3/4.0) * kõrgus)), (x+laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

fon=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
majavärv=[r,g,b]


pind=pygame.display.set_mode([640,480]) #Размер окна
pygame.display.set_caption("Juhuslikud objektid") #Название окна
pind.fill(fon) #Цвет фона, окна

ristkülik=pygame.Rect(300,220,100,178) #Дверь
pygame.draw.rect(pind,(139,69,19),ristkülik) 

lill=pygame.Rect(300,220,100,100)
pygame.draw.ellipse(pind,(255,255,0),lill)

Maja(100,400,300,400,pind,majavärv)
pygame.display.flip()

for i in range(10):
    #värv
    #color=random.choice(varv)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    varv=[r,g,b]
    #suurus
    laius=random.randint(10,50)
    kõrgus=random.randint(10,50)
    #pikkus=random.randint(10,50)
    #asukoht
    x=random.randint(0,640-laius)
    y=random.randint(0,480-kõrgus)
    
    pygame.draw.rect(pind,varv,[x,y,laius,kõrgus])

    pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        sys.exit()

pygame.quit()