import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan

def get_neighbors(node, n):
    x, y = node
    neighbors = []
    if x > 0: neighbors.append((x-1, y))
    if x < n-1: neighbors.append((x+1, y))
    if y > 0: neighbors.append((x, y-1))
    if y < n-1: neighbors.append((x, y+1))
    return neighbors

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    path.reverse()
    return path

def astar(grid, start, goal):
    n = len(grid)

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    nodes_explored = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        nodes_explored += 1

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, nodes_explored

        for neighbor in get_neighbors(current, n):
            x, y = neighbor
            if grid[x][y] == 1:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None, nodes_explored
