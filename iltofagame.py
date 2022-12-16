

import pygame
import random
pygame.init()

SCHERMO = pygame.display.set_mode((288, 512))



# =================================================================================== ASSET


background = pygame.image.load("./images/starsbg.png")
player = pygame.image.load("./images/alien.png")


# =================================================================================== SETUP

def setup():
    global status, playerx, playery, playerdir, speed, steer, lives, level, score
    # status 0 intro 1 menu 2 ingioco
    status=0

    # player
    playerx = 200
    playery = 200
    playerdir = True
    speed = 30
    steer = 4

    lives = 0
    level = 1
    score = 0



def draw():
        
    pass
    
def update():
    global status, playerx, playery, playerdir, speed, steer, lives, level, score
    
# =================================================================================== Aggiorna Schermo

    SCHERMO.blit(background, (0, 0))
    SCHERMO.blit(player, (playerx, playery))



# =================================================================================== CONTROLLI

    if keyboard.left:
        playerdir= False
    else:
        playerdir = True
        
    if playerdir == True:
        playerx += 4
    else:
        playerx -= 4
    
setup()


