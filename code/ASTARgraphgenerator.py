import matplotlib.pyplot as plt

def plot_results(results):
    sizes = [r["size"] for r in results]
    times = [r["avg_time"] for r in results]
    nodes = [r["avg_nodes"] for r in results]
    paths = [r["avg_path"] for r in results]
    success = [r["success_rate"] for r in results]

    # Runtime Graph
    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Maze Size (n x n)")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("A* Runtime vs Maze Size")
    plt.grid()
    plt.savefig("runtime.png")
    plt.close()

    # Nodes Explored Graph
    plt.figure()
    plt.plot(sizes, nodes, marker='o')
    plt.xlabel("Maze Size")
    plt.ylabel("Nodes Explored")
    plt.title("A* Nodes Explored vs Maze Size")
    plt.grid()
    plt.savefig("nodes.png")
    plt.close()

    # Path Length Graph
    plt.figure()
    plt.plot(sizes, paths, marker='o')
    plt.xlabel("Maze Size")
    plt.ylabel("Path Length")
    plt.title("A* Path Length vs Maze Size")
    plt.grid()
    plt.savefig("path.png")
    plt.close()

    # Success Rate
    plt.figure()
    plt.plot(sizes, success, marker='o')
    plt.xlabel("Maze Size")
    plt.ylabel("Success Rate")
    plt.title("A* Success Rate vs Maze Size")
    plt.grid()
    plt.savefig("success.png")
    plt.close()

    plt.show()