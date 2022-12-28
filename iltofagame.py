
import pgzero
import pygame
import random
import math
pygame.init()


WIDTH = 300
HEIGHT = 500
SCHERMO = pygame.display.set_mode((300, 500))

status=1



# =================================================================================== SETUP

background = pygame.image.load("./images/road.png")
background2 = pygame.image.load("./images/road.png")
player = pygame.image.load("./images/player.png")

# def setup():
# status 0 intro 1 menu 2 ingioco
status=1

# player
playerx = 100
playery = 400
playerdir = True
speed = 2
steer = 4

lives = 0
level = 1
score = 0

scrolly=0+background.get_height()
scrolly2=0
inputs=""


# =================================================================================== CONTROLLI
def on_mouse_down(pos, button):
    global inputs
    if pos[0] <= (WIDTH/2):
        inputs+="left"
    if pos[0] > (WIDTH/2):
        inputs+="down"
    if pos[1] < (HEIGHT/5):
        inputs+="escape"
	

def getkeys():
    global status, playerx, playery, playerdir, speed, steer, lives, level, score, inputs

    if keyboard.left:
        inputs+="left"
    if keyboard.down:
        inputs+="down"
    if keyboard.escape:
        inputs+="escape"


    if "left" in inputs:
        playerdir = False
    else:
        playerdir = True

#    if keyboard.up and speed < 10: accelerare

    if "down" in inputs and speed > 2:
        speed-=1
    elif speed <15:
        speed+=1


    if status == 1:
        if playerdir == True and playerx < 200 :
            playerx += steer
        if playerdir == False and playerx > 20 :
            playerx -= steer

    if inputs == "escape":
        if status == 0:
            exit()
        if status == 1:
            status = 0
#            setup()

    inputs = ""


def draw():
    pass


def scrolling():
    global status, playerx, playery, playerdir, speed, steer, lives, level, score, inputs
    global scrolly, scrolly2

    # Calcolo scrolling
    scrolly+=speed
    if scrolly> HEIGHT:
        scrolly=0- background.get_height() - 5
    scrolly2+=speed
    if scrolly2> HEIGHT:
        scrolly2=0- background2.get_height() - 5

    # Aggliornamento strada
    SCHERMO.blit(background, (0, scrolly))
    SCHERMO.blit(background2, (0, scrolly2))
    SCHERMO.blit(player, (playerx, playery))




# =================================================================================== Aggiorna Schermo
def update():
    global status, playerx, playery, playerdir, speed, steer, lives, level, score, inputs
    global scrolly,scrolly2

    pygame.display.update()
    scrolling()
    getkeys()