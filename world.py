import argparse
import random
import sys

from agents.agent import Agent
from utilities import preferences

tests = 100
max_iterations = 10,000

def setup(num_of_agents, states, agents: [], rand):
    """
    This setup function runs before any other part of the code. Starting with
    the creation of agents and the initialisation of relevant variables.
    """

    init_preference = preferences.uniform_pref_generator

    agents += [Agent(init_preference(states, rand)) for x in range(num_of_agents)]

    return


def main_loop():
    return


def main():

    # Parse the arguments of the program.
    parser = argparse.ArgumentParser(description="Preference-based distributed decision-making in a multi-agent environment.")
    # Number of agents.
    parser.add_argument("agents", type=int)
    # Number of states.
    parser.add_argument("states", type=int)
    # Random seeding
    parser.add_argument("-r", "--random", type=bool, help="Random seeding of the RNG.")
    arguments = parser.parse_args()

    agents = list()

    # Create an instance of a RNG that is either seeded for consistency of simulation
    # results, or create using a random seed for further testing.
    rand = random.Random().seed(128) if not arguments.random else random.Random().seed()

    # Initial setup of agents and environment.
    setup(arguments.agents, arguments.states, agents, rand)

    # Main loop of the experiments.
    main_loop()

    # Recording of results.


    sys.exit(1)


if __name__ == "__main__":
    main()

