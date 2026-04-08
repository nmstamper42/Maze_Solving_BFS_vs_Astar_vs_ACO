import time
from mazegenerator import generate_maze
from astarimplementation import astar

def run_experiment(sizes, trials=20):
    results = []

    for n in sizes:
        print(f"Running size {n}x{n}...")

        total_time = 0
        total_nodes = 0
        total_path = 0
        success_count = 0

        for _ in range(trials):
            grid = generate_maze(n)

            start = (0, 0)
            goal = (n-1, n-1)

            start_time = time.perf_counter()
            path, nodes = astar(grid, start, goal)
            end_time = time.perf_counter()

            total_time += (end_time - start_time)
            total_nodes += nodes

            if path:
                success_count += 1
                total_path += len(path)

        results.append({
            "size": n,
            "avg_time": total_time / trials,
            "avg_nodes": total_nodes / trials,
            "avg_path": total_path / max(success_count, 1),
            "success_rate": success_count / trials
        })

    return results