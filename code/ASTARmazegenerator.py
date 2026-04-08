import random

def generate_maze(n, wall_prob=0.3):
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if random.random() < wall_prob:
                grid[i][j] = 1  # wall

    # Ensure start and goal are open
    grid[0][0] = 0
    grid[n-1][n-1] = 0

    return grid