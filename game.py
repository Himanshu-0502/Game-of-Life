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
        grid[row, col] = 1
    return grid.tolist()

def alive_neighbors(grid, x, y, size):
    """Count the number of alive neighbors around a given cell."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = (x + dx) % size, (y + dy) % size
        count += grid[nx][ny]
    return count

def update_grid(grid):
    """Update the grid based on Conway's Game of Life rules."""
    next_grid = np.array(grid)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            total = alive_neighbors(grid, i, j, GRID_SIZE)
            if grid[i][j] == 1:
                if total == 2 or total == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0
            else:
                if total == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0
    return next_grid.tolist()