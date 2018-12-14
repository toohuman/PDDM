import argparse
import random
import sys

import numpy as np

from agents.agent import Agent
from utilities import operators
from utilities import preferences

tests = 100
max_iterations = 10,000

mode = "symmetric" # ["symmetric" | "asymmetric"]

# Set the initialisation function for agent preferences: [uniform, other]
init_preferences = preferences.uniform_pref_generator

def setup(num_of_agents, states, agents: [], rand):
    """
    This setup function runs before any other part of the code. Starting with
    the creation of agents and the initialisation of relevant variables.
    """

    agents += [Agent(init_preferences(states, rand)) for x in range(num_of_agents)]

    return

def main_loop(agents: [], states, mode, rand):
    """
    The main loop performs various actions in sequence until certain conditions are
    met, or the maximum number of iterations is reached.
    """

    # Agents receive evidence and perform evidential updating
    evidence = np.full((states, states), -1, int)
    index_i = random.randint(0, states - 1)
    index_j = index_i
    while index_j == index_i:
        index_j = random.randint(0, states - 1)

    print(evidence)


    # Agents then combine at random

    # Symmetric
    if mode == "symmetric":
        agent1 = agents[random.randint(0,len(agents) - 1)]
        agent2 = agent1
        while agent2 == agent1:
            agent2 = agents[random.randint(0,len(agents) - 1)]

        print(operators.combine(agent1.preferences, agent2.preferences))

    # Asymmetric
    # if mode == "asymmetric":

    return


def main():

    # Parse the arguments of the program, e.g., agents, states, random init.
    parser = argparse.ArgumentParser(description="Preference-based distributed decision-making in a multi-agent environment.")
    parser.add_argument("agents", type=int)
    parser.add_argument("states", type=int)
    parser.add_argument("-r", "--random", type=bool, help="Random seeding of the RNG.")
    arguments = parser.parse_args()

    rand = random.Random().seed(128) if not arguments.random \
                                     else random.Random().seed()

    # Repeat the setup and loop for the number of simulation runs required
    for test in range(tests):
        agents = list()
        # Create an instance of a RNG that is either seeded for consistency of simulation
        # results, or create using a random seed for further testing.

        # Initial setup of agents and environment.
        setup(arguments.agents, arguments.states, agents, rand)

        # Main loop of the experiments.
        main_loop(agents, arguments.states, mode, rand)

    # Recording of results.


    sys.exit(1)


if __name__ == "__main__":
    main()

