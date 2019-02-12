import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-darkgrid")
import matplotlib.cm as cm

PERC_LOWER = 10
PERC_UPPER = 90

cmap = cm.get_cmap("magma")

states_set = [5, 10, 20, 30, 40, 50]
agents_set = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
evidence_rates = [0.0, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0]
er = 0.01

result_directory = "../../results/test_results/pddm/"

heatmap_results = [[0.0 for x in states_set] for y in agents_set]
print(heatmap_results)

for i, agents in enumerate(agents_set):
    for j, states in enumerate(states_set):
        file_name_parts = ["loss", agents, "agents", states, "states", "{:.3f}".format(er), "er"]
        file_ext = ".csv"
        file_name = "_".join(map(lambda x: str(x), file_name_parts)) + file_ext

        steady_state_results = []

        try:
            with open(result_directory + file_name, "r") as file:
                for line in file:
                    steady_state_results = line

            steady_state_results = [float(x) for x in steady_state_results.strip().split(",")]

            average_loss = np.average(steady_state_results)
            print(average_loss)

            heatmap_results[i][j] = average_loss

        except FileNotFoundError:
            # Add obvious missing entry into final results array here
            heatmap_results[i][j] = -1.0

print(heatmap_results)