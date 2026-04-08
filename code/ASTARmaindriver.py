from experimentrunner import run_experiment
from graphgenerator import plot_results

if __name__ == "__main__":
    sizes = [10, 20, 40, 80]

    results = run_experiment(sizes, trials=20)

    for r in results:
        print(r)

    plot_results(results)