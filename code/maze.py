import random
random.seed(42)

def generate_maze(n, wall_prob=0.2):
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if random.random() < wall_prob:
                grid[i][j] = 1

    grid[0][0] = 0
    grid[n-1][n-1] = 0

    return grid