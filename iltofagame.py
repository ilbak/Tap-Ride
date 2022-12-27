

import pygame
import random
pygame.init()

WIDTH = 300
HEIGHT = 500
SCHERMO = pygame.display.set_mode((288, 512))



# =================================================================================== ASSET


background = pygame.image.load("./images/starsbg.png")
player = pygame.image.load("./images/alien.png")


# =================================================================================== SETUP

global status, playerx, playery, playerdir, speed, steer, lives, level, score
# status 0 intro 1 menu 2 ingioco
status=0

# player
playerx = 200
playery = 400
playerdir = True
speed = 30
steer = 4

lives = 0
level = 1
score = 0

# margine sinistro e margine destro
stageleft = 20
stageright = WIDTH - 50



def draw():

    pass

def update():
    global status, playerx, playery, playerdir, speed, steer, lives, level, score
    global stageleft, stageright

# =================================================================================== Aggiorna Schermo

    SCHERMO.blit(background, (0, 0))
    SCHERMO.blit(player, (playerx, playery))



# =================================================================================== CONTROLLI

    if keyboard.left:
        playerdir= False
    else:
        playerdir = True

    if playerdir == True and playerx < stageright:
        playerx += 4
    if playerdir == False and playerx > stageleft:
        playerx -= 4


