import argparse
import math
import random
import sys

import numpy as np

from agents.agent import Agent
from utilities import operators
from utilities import preferences

tests = 100
max_iterations = 10000

mode = "symmetric" # ["symmetric" | "asymmetric"]
demo_mode = True

evidence_rate = 1/100

# Set the initialisation function for agent preferences: [uniform, other]
init_preferences = preferences.ignorant_pref_generator

def setup(num_of_agents, states, agents: [], random_instance):
    """
    This setup function runs before any other part of the code. Starting with
    the creation of agents and the initialisation of relevant variables.
    """

    agents += [Agent(init_preferences(states)) for x in range(num_of_agents)]

    return

def main_loop(agents: [], states: int, mode: str, random_instance):
    """
    The main loop performs various actions in sequence until certain conditions are
    met, or the maximum number of iterations is reached.
    """

    # For each agent, generate a random piece of evidence and have the agent perform
    # evidential updating
    reached_convergence = True
    for agent in agents:
        # Currently, just testing with random evidence
        evidence = preferences.random_evidence(states, random_instance)

        # print(agent.preferences)

        if random_instance.random() <= evidence_rate:
            agent.evidential_updating(operators.combine(agent.preferences, evidence))

        # print(agent.preferences)

        agent.update()

        # print(agent.preferences)

        # print("-----------------------")

        reached_convergence &= agent.steady_state()

    if reached_convergence:
        return True

    #################################
    # Agents then combine at random #
    #################################

    # Symmetric
    if mode == "symmetric":
        agent1 = agents[random.randint(0,len(agents) - 1)]
        agent2 = agent1
        while agent2 == agent1:
            agent2 = agents[random.randint(0,len(agents) - 1)]

        new_preference = operators.combine(agent1.preferences, agent2.preferences)
        # print(new_preference)
        # Symmetric, so both agents adopt the combination preference
        agent1.update_preferences(new_preference)
        agent2.update_preferences(new_preference)

    # Asymmetric
    # if mode == "asymmetric":

    return False


def main():

    # Parse the arguments of the program, e.g., agents, states, random init.
    parser = argparse.ArgumentParser(description="Preference-based distributed\
    decision-making in a multi-agent environment.")
    parser.add_argument("agents", type=int)
    parser.add_argument("states", type=int)
    parser.add_argument("-r", "--random", type=bool, help="Random seeding of the RNG.")
    arguments = parser.parse_args()

    random_instance = random.Random()
    # This needs to be fixed using GETSTATE and SETSTATE
    random_instance.seed(128) if arguments.random == None else random_instance.seed()

    # Set up the collecting of results


    # Repeat the setup and loop for the number of simulation runs required
    for test in range(tests):
        agents = list()
        # Create an instance of a RNG that is either seeded for consistency of simulation
        # results, or create using a random seed for further testing.

        # Initial setup of agents and environment.
        setup(arguments.agents, arguments.states, agents, random_instance)

        # Main loop of the experiments.
        for iteration in range(max_iterations):
            if main_loop(agents, arguments.states, mode, random_instance):
                print(test, ":", iteration)
                break

    # Recording of results.
    # if demo_mode:
        # Output plots while running simulations, but do not record the results.
    # else:
        # Record the results but skip the plotting.


    sys.exit(1)


if __name__ == "__main__":
    main()

