
import pgzero
import pygame
import random
import math
pygame.init()


WIDTH = 300
HEIGHT = 500
SCHERMO = pygame.display.set_mode((300, 500))


# =================================================================================== SETUP

# status 0 intro 1 menu 2 ingioco
status=1

# Scrolling background
background = pygame.image.load("./images/road.png")
background2 = pygame.image.load("./images/road2.png")





oil = Actor( "oil",  (0,0) )
oils=[]

rock= Actor("rock", (0,0) )
rocks=[]


barrel= Actor("barrel", (0,0) )
barrels=[]

arrwhite = Actor("arrow_white", (0,0))
arrswhite = []

arrwhite = Actor("arrow_yellow", (0,0))
arrsyellow = []

tapride = Actor("tapride", (WIDTH/2, HEIGHT/2) )



# player

player = Actor("player", (60, HEIGHT-80) )

scrolly=0+background.get_height()
scrolly2=0
inputs=""

framecount=0

def setup():
#reset dei lavori di gioco
    global status, playerdir, speed, topspeed, steer, lives, level, score, inputs, scrolly, scrolly2, framecount, fuel, topscore

    playerdir = True
    speed = 1
    topspeed = 2
    steer = 4
    fuel=100
    lives = 3
    metri = 1
    score = 0
    topscore= 0

setup()

# Musica! job
sounds.arcade.play()

# =================================================================================== CONTROLLI

def getkeys():
    global status, playerdir, speed, topspeed, steer, lives, level, score, inputs, scrolly, scrolly2, framecount, fuel, topscore

    if keyboard.left:
        inputs+="left"
    if keyboard.down:
        inputs+="down"
    if keyboard.up:
        inputs+="up"
    if keyboard.right:
        inputs+="right"
    if keyboard.escape:
        exit()

    if keyboard.up:
        status=1
    if keyboard.right:
        status=2


    if "left" in inputs:
        playerdir = False
    else:
        playerdir = True

    if keyboard.up:
        pass

    if "down" in inputs and speed > 2:
        speed-=0.2
    elif speed < topspeed:
        speed+=0.5


    if status == 2:

        if playerdir == True and player.x < (WIDTH-50) :
            player.x += steer
        if playerdir == False and player.x > 50 :
            player.x -= steer

    if "escape" in inputs:
        inputs = ""
        barrel= Actor("barrel", (0,0) )
        barrels.append(barrel)


        if status == 0:
            pass
        if status == 1:
            status = 0
        if status == 2:
            status = 1



# =================================================================================== DRAW

def draw():
    global status, playerdir, speed, topspeed, steer, lives, level, score, inputs, scrolly, scrolly2, framecount, fuel, topscore
    pygame.display.update()
    # Aggliornamento strada

    SCHERMO.blit(background, (0, scrolly))
    SCHERMO.blit(background2, (0, scrolly2))

    if status == 2:
        player.draw()


# Gestione COLLISIONI
    for barrel in barrels:
        if barrel.y < HEIGHT:
            barrel.draw()
            if barrel.colliderect(player) and status == 2:
                barrels.remove(barrel)
                sounds.powerup.play()
#                print ("barrel collide")
                fuel = 100
        else:
            barrels.remove(barrel)


    for rock in rocks:
        if rock.y < HEIGHT:
            rock.draw()
            if rock.colliderect(player) and status == 2:
                sounds.rock.play()
                rocks.remove(rock)
#                print ("rock collide")
                lives-=1
                speed=0
                topspeed=topspeed/2
        else:
            rocks.remove(rock)


# Aggiorna UI
    if status == 2:
        if score < topscore:
            screen.draw.text("Lives "+str(lives)+" Score "+str(score)+" Fuel " +str(fuel)+"%", (10,10))
        if score > topscore:
            topscore=score
            screen.draw.text("Lives "+str(lives)+" TOP Score "+str(score)+" Fuel " +str(fuel)+"%", (10,10))
    if status < 2:
        screen.draw.text("Top Score "+str(topscore) , (10,10))
        screen.draw.text("KiRoDe Software presents:", (40,70))
        screen.draw.text("Press UP to Play!", (80,HEIGHT-50))


# Se status 1 metti il titolo
    if status == 1:
        tapride.draw()





def scrolling():
    global status, playerdir, speed, topspeed, steer, lives, level, score, inputs, scrolly, scrolly2, framecount, fuel, topscore

    # Calcolo scrolling
    scrolly+=speed
    if scrolly> HEIGHT:
        scrolly=0- background.get_height() - 5
    scrolly2+=speed
    if scrolly2> HEIGHT:
        scrolly2=0- background2.get_height() - 5

# Scrolling degli oggetti
    for barrel in barrels:
        barrel.y+=speed
    for rock in rocks:
        rock.y+=speed






# =================================================================================== UPDATE
def update():
    global status, playerdir, speed, topspeed, steer, lives, level, score, inputs, scrolly, scrolly2, framecount, fuel, topscore

    scrolling()
    getkeys()

# se finisce il carburante game over
    if fuel < 1:
        status=1

# se non hai lives game over
    if lives < 1:
        status=1

# se sei al menu e premi up ricominci il gioco
    if status == 1:
        # print("Menu di gioco")
        if "up" in inputs:
            setup()
            status=2

    framecount+=1
# secondo
    if framecount > 59+ (topspeed/3) and status == 2:
        topspeed+=1
        framecount=0
        junk=0

    # genera item casuale
        if status == 2:
            junk = random.randint(0,10)

        if junk > 7 and junk < 10:
            barrel = Actor("barrel", pos=(random.randint(50, 250), -40))
            barrels.append(barrel)
        if junk > 4 and junk < 8:
            rock = Actor("rock", pos=(random.randint(50, 250), -40))
            rocks.append(rock)

# aggiorna i valori in base allo status
        if status == 2:
            if "up" in inputs:
                lives-=1
            if "down" in inputs:
                score-=1
            else:
                score+=1
            fuel-=1
        if status < 2:
            pass


# Resetta input
    inputs = ""