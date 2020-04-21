# -*- coding: utf-8 -*-

import numpy as np
import pygame
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~    Colors   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

bg_color = 20, 20, 20
dead_color = ( 120, 120, 120 )
live_color = ( 255, 255, 255 )
line_width = 1

screen.fill(bg_color)

N = 30
nx, ny = N, N
dimCW = width / nx
dimCH = height / ny

startMatrix = np.zeros((nx, ny))
start = True
####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~    Rules   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################
def lifeordead(stateMatrix,x,y):
    # Sum alive neighbors
    n_neighbors = stateMatrix[(x-1) % nx,(y-1) % ny] + \
                  stateMatrix[(x-1) % nx,(y) % ny] + \
                  stateMatrix[(x-1) % nx,(y+1) % ny] + \
                  stateMatrix[(x) % nx,(y+1) % ny] + \
                  stateMatrix[(x+1) % nx,(y+1) % ny] + \
                  stateMatrix[(x+1) % nx,(y) % ny] + \
                  stateMatrix[(x+1) % nx,(y-1) % ny] + \
                  stateMatrix[(x) % nx,(y-1) % ny]
    if stateMatrix[x, y] == 0 and n_neighbors == 3:
        return 1
    elif stateMatrix[x, y] == 1 and (
        n_neighbors < 2 or n_neighbors > 3
        ):
        return 0
    else:
        stateMatrix[x, y]

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~Initial system~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
            newStateMatrix[x, y] = lifeordead(stateMatrix, x, y)
            dots = [
                (x) * dimCW,   (y) * dimCH,
                (x+1) * dimCW, (y) * dimCH,
                (x+1) * dimCW, (y+1) * dimCH,
                (x) * dimCW,   (y+1) * dimCH,
            ]
            if newStateMatrix[x, y]:
                pygame.draw.polygon(screen, live_color, dots, 0)
            else:
                pygame.draw.polygon(screen, dead_color,
                                    dots, line_width)
    stateMatrix = np.copy(newStateMatrix)