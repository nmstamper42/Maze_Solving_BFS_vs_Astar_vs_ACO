import random
from astar import astar
from gbfs import gbfs
from bfs import bfs
from experiment import run_experiment
from graphs import plot_all_comparisons


def main():
    random.seed(42)

    sizes = [10, 20, 40, 80]

    print("Running A*...")
    astar_results = run_experiment(astar, sizes, trials=20)

    print("Running GBFS...")
    gbfs_results = run_experiment(gbfs, sizes, trials=20)

    print("Running BFS...")
    bfs_results = run_experiment(bfs, sizes, trials=20)

    print("\nA* Results:")
    for r in astar_results:
        print(r)

    print("\nGBFS Results:")
    for r in gbfs_results:
        print(r)

    print("\nBFS Results:")
    for r in bfs_results:
        print(r)

    plot_all_comparisons(astar_results, gbfs_results, bfs_results)

    print("\nAll experiments complete. Graphs saved.")


if __name__ == "__main__":
    main()