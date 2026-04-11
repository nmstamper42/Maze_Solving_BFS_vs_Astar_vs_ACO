import matplotlib.pyplot as plt

def plot_results(results, label):
    sizes = [r["size"] for r in results]
    times = [r["avg_time"] for r in results]
    nodes = [r["avg_nodes"] for r in results]

    plt.figure()
    plt.plot(sizes, times, marker='o', label=label)
    plt.xlabel("Maze Size")
    plt.ylabel("Runtime")
    plt.title("Runtime Comparison")
    plt.legend()
    plt.savefig("runtime.png")
    plt.close()

    plt.figure()
    plt.plot(sizes, nodes, marker='o', label=label)
    plt.xlabel("Maze Size")
    plt.ylabel("Nodes Explored")
    plt.title("Nodes Comparison")
    plt.legend()
    plt.savefig("nodes.png")
    plt.close()

import matplotlib.pyplot as plt

def plot_all_comparisons(astar_results, gbfs_results, bfs_results):
    sizes = [r["size"] for r in astar_results]

    def extract(results, key):
        return [r[key] for r in results]

    astar_time = extract(astar_results, "avg_time")
    gbfs_time = extract(gbfs_results, "avg_time")
    bfs_time = extract(bfs_results, "avg_time")

    astar_nodes = extract(astar_results, "avg_nodes")
    gbfs_nodes = extract(gbfs_results, "avg_nodes")
    bfs_nodes = extract(bfs_results, "avg_nodes")

    astar_path = extract(astar_results, "avg_path")
    gbfs_path = extract(gbfs_results, "avg_path")
    bfs_path = extract(bfs_results, "avg_path")

    astar_success = extract(astar_results, "success_rate")
    gbfs_success = extract(gbfs_results, "success_rate")
    bfs_success = extract(bfs_results, "success_rate")

    plt.figure()
    plt.plot(sizes, astar_time, marker='o', label="A*")
    plt.plot(sizes, gbfs_time, marker='o', label="GBFS")
    plt.plot(sizes, bfs_time, marker='o', label="BFS")
    plt.xlabel("Maze Size (n x n)")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("Runtime Comparison")
    plt.legend()
    plt.grid()
    plt.savefig("final_runtime.png")
    plt.close()

    plt.figure()
    plt.plot(sizes, astar_nodes, marker='o', label="A*")
    plt.plot(sizes, gbfs_nodes, marker='o', label="GBFS")
    plt.plot(sizes, bfs_nodes, marker='o', label="BFS")
    plt.xlabel("Maze Size")
    plt.ylabel("Nodes Explored")
    plt.title("Nodes Explored Comparison")
    plt.legend()
    plt.grid()
    plt.savefig("final_nodes.png")
    plt.close()

    plt.figure()
    plt.plot(sizes, astar_path, marker='o', label="A*")
    plt.plot(sizes, gbfs_path, marker='o', label="GBFS")
    plt.plot(sizes, bfs_path, marker='o', label="BFS")
    plt.xlabel("Maze Size")
    plt.ylabel("Path Length")
    plt.title("Path Length Comparison")
    plt.legend()
    plt.grid()
    plt.savefig("final_path.png")
    plt.close()

    plt.figure()
    plt.plot(sizes, astar_success, marker='o', label="A*")
    plt.plot(sizes, gbfs_success, marker='o', label="GBFS")
    plt.plot(sizes, bfs_success, marker='o', label="BFS")
    plt.xlabel("Maze Size")
    plt.ylabel("Success Rate")
    plt.title("Success Rate Comparison")
    plt.legend()
    plt.grid()
    plt.savefig("final_success.png")
    plt.close()