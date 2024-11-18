import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = 'HomeWork Game'

pylon_num = 8
pylons = []
next_pylons = 0
lines = []

starttime = 0
totaltime = 0
endtime = 0


def start():
    global starttime
    for i in range(0,pylon_num):
        sat = Actor('pylon')
        sat.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        pylons.append(sat)
    
    starttime = time()


def draw():
    global totaltime

    num = 1

    screen.blit('desert',(0,0))

    for sat in pylons:
        sat.draw()
        screen.draw.text(str(num),(sat.pos[0],sat.pos[1]+20))
        num = num + 1
    
    for line in lines:
        screen.draw.line(line[0],line[1],(0,0,0))

    if next_pylons < pylon_num:
        totaltime = time() - starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize = 30)

    else:
       screen.draw.text(str(round(totaltime,1)),(10,10),fontsize = 30)

    if next_pylons == 8:
        screen.draw.text("Good Job",(300,300), fontsize = 55)

def update():
    pass
        
def on_mouse_down(pos):
    global next_pylons, lines
    if next_pylons < pylon_num:
        if pylons[next_pylons].collidepoint(pos):
            if next_pylons:
                lines.append((pylons[next_pylons-1].pos, pylons[next_pylons].pos))
            next_pylons= next_pylons + 1
        else:
            lines = []
            next_pylons= 0








start()
pgzrun.go()

