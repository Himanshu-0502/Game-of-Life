import numpy as np

GRID_SIZE = 32
ALIVE_CELLS = 256

def initialize_grid():
    """Initialize the grid with a fixed number of alive cells randomly placed."""
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    alive_cells = np.random.choice(GRID_SIZE * GRID_SIZE, ALIVE_CELLS, replace=False)
    for cell in alive_cells:
        row = cell // GRID_SIZE
        col = cell % GRID_SIZE
        grid[row][col] = 1
    return grid.tolist()

def update_grid(grid):
    """Update the grid based on Conway's Game of Life rules."""
    alive = {}
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 1:
                alive[(i, j)] = True

    next_alive = {}
    for cell in alive:
        x, y = cell
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = (x + dx) % GRID_SIZE, (y + dy) % GRID_SIZE
                next_alive[(nx, ny)] = next_alive.get((nx, ny), 0) + 1
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if next_alive.get((i, j), 0) == 3 or next_alive.get((i, j), 0) == 2 and (i, j) in alive:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid