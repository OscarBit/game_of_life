# -*- coding: utf-8 -*-

import numpy as np
import pygame
import time
import sys

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
  
####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~    Colors   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

bg_color = 60, 60, 60
dead_color = ( 120, 120, 120 )
live_color = ( 255, 255, 255 )
line_width = 1

N = 30
nx, ny = N, N
dimCW = width / nx
dimCH = height / ny

startMatrix = np.zeros((nx, ny))
start = True
####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~    Rules   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################
def lifeordead(Matrix,x,y):
    # Sum alive neighbors
    n_neighbors = (Matrix[(x-1) % nx,(y-1) % ny] + 
    Matrix[(x-1) % nx,(y) % ny] +
    Matrix[(x-1) % nx,(y+1) % ny] +
    Matrix[(x) % nx,(y+1) % ny] +
    Matrix[(x+1) % nx,(y+1) % ny] +
    Matrix[(x+1) % nx,(y) % ny] +
    Matrix[(x+1) % nx,(y-1) % ny] +
    Matrix[(x) % nx,(y-1) % ny])
    if Matrix[x, y] == 0 and n_neighbors == 3:
        return 1
    elif Matrix[x, y] == 1 and (
        n_neighbors < 2 or n_neighbors > 3
        ):
        return 0
    else:
        return Matrix[x, y]

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~Initial system~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################
startMatrix[10,1] = 1
startMatrix[10,2] = 1
startMatrix[10,3] = 1

startMatrix[21,21] = 1
startMatrix[22,22] = 1
startMatrix[22,23] = 1
startMatrix[21,23] = 1
startMatrix[20,23] = 1

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~Fun begins! ~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################
pauseExect = False

while True:
    if start:
        stateMatrix = np.copy(startMatrix)
        start = False

    newStateMatrix = np.copy(stateMatrix)

    # Events functions, PAUSE, QUIT, DRAW
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Three components vector (RB,SB,LB)

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            lifeX, lifeY = (int(np.floor(posX / dimCW)),
                            int(np.floor(posY / dimCH)))
            newStateMatrix[lifeX, lifeY] = not mouseClick[2]

    # If it is puased do not refill for show the current state
    if not pauseExect:
        screen.fill(bg_color)

    for (x, y), i in np.ndenumerate(z):
    #for x in range(0, nx):
        #for y in range(0,ny):
        if not pauseExect:
            dots = [
                ((x) * dimCW,   (y) * dimCH),
                ((x+1) * dimCW, (y) * dimCH),
                ((x+1) * dimCW, (y+1) * dimCH),
                ((x) * dimCW,   (y+1) * dimCH),
            ]
            newStateMatrix[x, y] = lifeordead(stateMatrix, x, y)
            if newStateMatrix[x, y]:
                pygame.draw.polygon(screen, live_color, dots, 0)
            else:
                pygame.draw.polygon(screen, dead_color,
                                    dots, line_width)
        else:
            # Draw in Pause 
            dots = [
                ((x) * dimCW,   (y) * dimCH),
                ((x+1) * dimCW, (y) * dimCH),
                ((x+1) * dimCW, (y+1) * dimCH),
                ((x) * dimCW,   (y+1) * dimCH),
            ]
            if newStateMatrix[x, y]:
                pygame.draw.polygon(screen, live_color, dots, 0)
            else:
                pygame.draw.polygon(screen, dead_color,
                                    dots, line_width)
    stateMatrix = np.copy(newStateMatrix)
    time.sleep(0.1)
    pygame.display.flip()