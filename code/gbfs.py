import heapq
from astar import heuristic, get_neighbors, reconstruct_path

def gbfs(grid, start, goal):
    n = len(grid)

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    visited = set()

    nodes_explored = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        nodes_explored += 1

        if current == goal:
            return reconstruct_path(came_from, current), nodes_explored

        visited.add(current)

        for neighbor in get_neighbors(current, n):
            x, y = neighbor
            if grid[x][y] == 1:
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                h = heuristic(neighbor, goal)
                heapq.heappush(open_set, (h, neighbor))

    return None, nodes_explored