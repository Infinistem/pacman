import pygame, random, sys, time
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC # use winsound for async


from Level import Level
from Pacman import Pacman
from Ghost import Ghost

WIDTH = 730
HEIGHT = 800
FPS = 100
TILE = 20
OFFSET = 60
gameOver = False  
game = True
gamePaused = False
play = True
# so that the fruits apper and disapper we need to keep track of time
startTime = 0
endTime = 0

button = pygame.Rect(280,30,140,30)
button1 = pygame.Rect(350,30,140,30)

def reset():
    pass
def victory():
    pass
def plays():
    global play
    PlaySound('Sounds\pacman_chomp.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)
    play = False
    print('played')
def renderText(font, txt, left, top, col):
    textobj = font.render(txt, 1, tuple(col))
    textrect = textobj.get_rect()
    textrect.topleft = (left, top)
    screen.blit(textobj, textrect)

pygame.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('Pacman!')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
font = pygame.font.SysFont(None, 30)
title = pygame.font.SysFont(None, 40)

starting = True
level = Level(screen)
c, r = level.getArrayCoords([350, 465])
prect = pygame.Rect(355, 465, 30, 30)
pacman = Pacman((355,465), level, prect)
ghosts = [Ghost(pygame.Rect(350, 325, 35, 35), "Blinky", level.ids, level, pacman),Ghost(pygame.Rect(315, 400, 35, 35), "Pinky", level.ids, level, pacman),Ghost(pygame.Rect(350, 400, 35, 35),"Inky", level.ids, level, pacman), Ghost(pygame.Rect(380, 400, 35, 35),"Clyde", level.ids, level, pacman)]
def colliderec(xvel, yvel): # column, row
    if play == True:
            plays()
    pacman.rect.x += xvel
    for sq in range(0, len(level.surfaces)):
        for x in level.surfaces[sq]:
            if pacman.rect.colliderect(x):
                if xvel < 0:  # We're moving to the left.
                    # Move the player out of the block.
                    pacman.rect.left = x.right
                elif xvel > 0:  # We're moving to the right.
                     pacman.rect.right = x.left
                break
    pacman.rect.y += yvel
    for sq in range(0, len(level.surfaces)):
        for x in level.surfaces[sq]:
            if pacman.rect.colliderect(x):
                if yvel < 0:  # We're moving to the left.
                    # Move the player out of the block.
                    pacman.rect.top = x.bottom
                elif yvel > 0:  # We're moving to the right.
                     pacman.rect.bottom = x.top
                break
    for pellet in level.circles:
        if pacman.rect.colliderect(pellet):
            row, column = level.getArrayCoords([pacman.rect.left, pacman.rect.top])
            if level.map[column][row] == 'Q':
                level.score += 10
            elif level.map[column][row] == 'O':
                level.score += 50
                level.scatterGhosts()
            elif level.map[column][row] == 'F':
                PlaySound('Sounds\pacman_eatfruit.wav', SND_ASYNC)
                if level.fruit == 'cherry': # dont do this! use an enum or dictonary instaed, this is bad programming. idk why i did it then lol
                    level.score += 100
                if level.fruit == 'berry':
                    level.score += 300
                if level.fruit == 'orange':
                    level.score += 500
                if level.fruit == 'apple':
                    level.score += 700
                if level.fruit == 'melon':
                    level.score += 1000
                if level.fruit == 'galaxian':
                    level.score += 2000
                if level.fruit == 'bell':
                    level.score += 3000
                if level.fruit == 'key':
                    level.score += 5000
                if level.fruit == 'poo':
                    level.score += 6900
                if level.fruit == 'crown':
                    victory()
            if level.score > 10000 and level.extraLive == False:
                level.lives += 'X'
                level.extraLive = True
            l = list(level.map[column])
            l[row] = 'N'
            level.map[column] = "".join(l)
            break
    for x in ghosts:
        if pacman.rect.colliderect(x):
            looselive()
    if roundover(): # reset for new level
        global starting
        level.reset()
        level.level += 1
        pacman.rect.top = 465
        pacman.rect.left = 355
        pacman.direction = 'W'
def roundover():
    for x in level.map:
        for y in list(x):
            if y == 'O' or y == 'Q':
                return False
    return True
def looselive():
    level.lives = level.lives[:-1]
    global starting
    deathSound = pygame.mixer.Sound('Sounds\pacman_death.wav')
    pacman.rect.top = 465
    pacman.rect.left = 355
    pacman.direction = 'W'
    deathSound.play()
    pygame.event.wait()
menubar = pygame.Rect(0, 0, WIDTH, OFFSET)
mySound = pygame.mixer.Sound('Sounds\pacman_beginning.wav')
image = pygame.image.load("Images\\pacman.png")
image = pygame.transform.scale(image, (30, 30))
while not gameOver:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (10,0,90), menubar)
    renderText(font,"Score: " + str(level.score),50, 10, (255,255,255))
    renderText(font,"Level: " + str(level.level),500, 10,(255,255,255))
    renderText(font,"Highscore: 0",50, 40,(255,255,255))
    renderText(font,"Lives:" + level.lives,500, 40,(255,255,255))

    renderText(title,"Pacman",300, 3,(250,250,0))
    pygame.draw.rect(screen, (40, 200, 100), button)
    renderText(font, "QUIT GAME", 290, 35, (255, 255, 255))
    level.render()
    if starting:
        
        mySound.play()
        pygame.event.wait()
        starting = False
        pacman.direction = 'W'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    reset()
                    continue
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w: # change directions
                pacman.direction = 'N'
            elif event.key == pygame.K_a:
                pacman.direction = 'W'
            elif event.key == pygame.K_d:
                pacman.direction = 'E'
            elif event.key == pygame.K_s:
                pacman.direction = 'S'    
    if game == True and starting == False:
        i, j = level.getArrayCoords([pacman.rect.left, pacman.rect.top])
        l = list(level.map[j])
        l[i] = 'N'
        #level.map[i] = "".join(l)# 
        #Note: Update code so that we have smooth tile movement! only change direction when the game detects an open area
        if level.map[j][i] == '2':
            print(level.map)
            pacman.rect = pygame.Rect(40, 400, 30, 30)
        elif level.map[j][i] == '1':
            print(0)
            pacman.rect = pygame.Rect(600, 400, 30, 30)
        if pacman.direction == 'W' and not pygame.mixer.get_busy():
            colliderec(-pacman.speed-1, 0)
        elif pacman.direction == 'N' and not pygame.mixer.get_busy():
            colliderec(0, -pacman.speed)
        elif pacman.direction == 'S' and not pygame.mixer.get_busy():
            colliderec(0, pacman.speed+1)
        elif pacman.direction == 'E' and not pygame.mixer.get_busy():
            colliderec(pacman.speed, 0)
        for x in ghosts: 
            x.findTarget() # first thing calculate the target for the ghost to go to
            x.findPathToTarget()
            x.followPath()
            image1 = pygame.image.load(x.sprite)
            image1 = pygame.transform.scale(image1, (30, 30))
            screen.blit(image1, x.rect)
        screen.blit(image, pacman.rect)
        pygame.display.flip()
        # move and draw pacman
    
    
    mainClock.tick(FPS)



