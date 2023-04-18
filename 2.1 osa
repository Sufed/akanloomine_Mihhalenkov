import pygame
import random
import sys

def Maja(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y- ((3/4.0) * kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0) * kõrgus), (x,y-((3/4.0) * kõrgus)), (x+laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)

def Uks(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y),(x,y-(1/2)*kõrgus),(x+(1/3)*laius,y-(1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,True,punktid,suurus)

def Aken(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y),(x,y-kõrgus),(x+laius,y-kõrgus),(x+laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,True,punktid,suurus)

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


#ristkülik=pygame.Rect(297,217,100,180)                            
#pygame.draw.rect(pind,(205,133,63),ristkülik)

#lil=pygame.Rect(300,300,15,15)
#pygame.draw.ellipse(pind, (250,250,0), lil)

#ristkülik=pygame.Rect(120,165,100,100)                            
#pygame.draw.rect(pind,(250,250,0),ristkülik)


Maja(100,400,300,400,pind,majavärv)
Uks(100,400,300,400,pind,majavärv)
Aken(250,300,100,100,pind,000) 
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
