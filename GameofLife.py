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

stateMatrix = np.zeros((nx, ny))

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~    Rules   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

def lifeordead(Matrix,x,y,state):
    """Function to update cell state.
    
    Args:
      Matrix: matrix of the system
      x, y: coordenates of cell
      state: 1 or 0, life or dead.
      
    Returns:
      New value for state of cell x,y
    """
    n_neighbors = (Matrix[(x-1) % nx,(y-1) % ny] + 
    Matrix[(x-1) % nx,(y) % ny] +
    Matrix[(x-1) % nx,(y+1) % ny] +
    Matrix[(x) % nx,(y+1) % ny] +
    Matrix[(x+1) % nx,(y+1) % ny] +
    Matrix[(x+1) % nx,(y) % ny] +
    Matrix[(x+1) % nx,(y-1) % ny] +
    Matrix[(x) % nx,(y-1) % ny])
    if not state and n_neighbors == 3:
        state = 1
    elif state and (
        n_neighbors < 2 or n_neighbors > 3
        ):
        state = 0
    else:
        pass
    return state


####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~Initial system~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

stateMatrix[10,1] = 1
stateMatrix[10,2] = 1
stateMatrix[10,3] = 1

stateMatrix[21,21] = 1
stateMatrix[22,22] = 1
stateMatrix[22,23] = 1
stateMatrix[21,23] = 1
stateMatrix[20,23] = 1

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~Fun begins! ~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################
pauseExect = False

while True:
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

    for (x, y), value in np.ndenumerate(stateMatrix):
        dots = [
            ((x) * dimCW,   (y) * dimCH),
            ((x+1) * dimCW, (y) * dimCH),
            ((x+1) * dimCW, (y+1) * dimCH),
            ((x) * dimCW,   (y+1) * dimCH),
        ]
        if not pauseExect:
            # Draw
            newStateMatrix[x, y] = lifeordead(
                stateMatrix, x, y, value,
                )
            if newStateMatrix[x, y]:
                pygame.draw.polygon(screen, live_color, dots, 0)
            else:
                pygame.draw.polygon(screen, dead_color,
                                    dots, line_width)
        else:
            # Draw in Pause 
            if value:
                pygame.draw.polygon(screen, live_color, dots, 0)
            else:
                pygame.draw.polygon(screen, dead_color,
                                    dots, line_width)
    stateMatrix = np.copy(newStateMatrix)
    time.sleep(0.1)
    pygame.display.flip()
