import pygame

# Functions

def evolution(cells, grid_size, neighbours_become_alive, neighbours_toSurvive):
    next_cells = list(cells)
    for i in range(grid_size):
        for j in range(grid_size):
            if cells[i*grid_size+j] == 0:
                next_cells[i*grid_size+j] = checkIfBecomesAlive(cells, i, j, grid_size, neighbours_become_alive)
            else:
                next_cells[i*grid_size+j] = checkIfSurvives(cells, i, j, grid_size, neighbours_toSurvive)
    return next_cells


def getLivingNeighbours(cells, posy, posx, grid_size):
    row_pos = posy*grid_size+posx
    living_neighbours = 0
    if posx > 0:
        if cells[row_pos-1]:
            living_neighbours += 1
        if posy > 0:
            if cells[row_pos-grid_size-1]:
                living_neighbours += 1
        if posy < grid_size-1:
            if cells[row_pos+grid_size-1]:
                living_neighbours += 1
    if posx < grid_size-1:
        if cells[row_pos+1]:
            living_neighbours += 1
        if posy > 0:
            if cells[row_pos-grid_size+1]:
                living_neighbours += 1
        if posy < grid_size-1:
            if cells[row_pos+grid_size+1]:
                living_neighbours += 1
    if posy > 0:
        if cells[row_pos-grid_size]:
            living_neighbours += 1
    if posy < grid_size-1:
        if cells[grid_size]:
            living_neighbours += 1

    return living_neighbours


def checkIfBecomesAlive(cells, posx, posy, grid_size, neighbours_become_alive):
    if getLivingNeighbours(cells, posx, posy, grid_size) in neighbours_become_alive:
        return 1
    return 0


def checkIfSurvives(cells, posx, posy, grid_size, neighbours_toSurvive):
    if getLivingNeighbours(cells, posx, posy, grid_size) in neighbours_toSurvive:
        return 1
    return 0


def drawGrid(display, cells, grid_size):
    blockSize = 1000/grid_size
    for x in range(grid_size):
        for y in range(grid_size):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            if cells[x*grid_size+y] == 0:
                pygame.draw.rect(display, (0, 0, 0), rect, 0)
            else:
                pygame.draw.rect(display, (0, 255, 0), rect, 0)
