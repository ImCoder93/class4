import pgzrun
import random 

WIDTH = 500
HEIGHT = 500

message=''
alien= Actor('alien')

def draw():
    screen.fill(color=(128,0,0))
    alien.draw()
    screen.draw.text(message, center=(350,40),fontsize=18)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message= 'good shot'
        alien.x=random.randint(50,450)
        alien.y=random.randint(50,450)


    else:
        message= 'missed shot'                                                      





pgzrun.go()
