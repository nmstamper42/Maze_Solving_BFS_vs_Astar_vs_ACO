from collections import deque
from astar import get_neighbors, reconstruct_path

def bfs(grid, start, goal):
    n = len(grid)

    queue = deque([start])
    visited = set([start])
    came_from = {}

    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            return reconstruct_path(came_from, current), nodes_explored

        for neighbor in get_neighbors(current, n):
            x, y = neighbor

            if grid[x][y] == 1:
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    return None, nodes_explored