import argparse
import random
import sys

from agents.agent import Agent
import utilities

tests = 100
max_iterations = 10,000

agents = []

def setup(num_of_agents):
    """
    This setup function runs before any other part of the code. Starting with
    the creation of agents and the initialisation of relevant variables.
    """

    random_pref = utilities.preferences.uniform_pref_generator

    agents = [Agent(random_pref(rand)) for x in range(num_of_agents)]

    return


def main_loop():
    return


def main():

    parser = argparse.ArgumentParser(description="Preference-based distributed decision-making in a multi-agent environment.")

    arguments = parser.parse_args()

    num_of_agents = 100

    # Initial setup of agents and environment
    setup(num_of_agents)

    # Main loop of the experiments
    main_loop()

    # Recording of results
    sys.exit(1)


if __name__ == "__main__":
    main()

