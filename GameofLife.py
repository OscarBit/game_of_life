# -*- coding: utf-8 -*-

import numpy as np
import pygame
import time

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

N = 5
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
startMatrix[2,1] = 1
startMatrix[2,2] = 1
startMatrix[2,3] = 1

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~Fun begins! ~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################
while True:
    if start:
        stateMatrix = np.copy(startMatrix)
        start = False
    newStateMatrix = np.copy(stateMatrix)
    screen.fill(bg_color)
    time.sleep(0.1)

    for x in range(0, nx):
        for y in range(0,ny):
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
    stateMatrix = np.copy(newStateMatrix)