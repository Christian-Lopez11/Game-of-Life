import pygame
import random
from utils import *

# Initializing Fixed Variables
GRID_SIZE = 100
NEIGHBOURS_TO_SURVIVE = [2, 3]
NEIGHBOURS_TO_BECOME_ALIVE = [3] 
PORCENTAGE_OF_CELLS_ALIVE = 50

# Game
def game():
    cells = []
    for i in range(GRID_SIZE**2):
        n = random.randint(1, 100)
        if n <= PORCENTAGE_OF_CELLS_ALIVE:
            cells.append(1)
        else:
            cells.append(0)

    pygame.init()
    display = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    FPS = 5
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((0, 0, 0))
        drawGrid(display, cells, GRID_SIZE)
        cells = evolution(cells, GRID_SIZE, NEIGHBOURS_TO_BECOME_ALIVE, NEIGHBOURS_TO_SURVIVE)

        pygame.display.update()
        clock.tick(FPS)


game()





