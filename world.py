import argparse
import math
import random
import sys

import numpy as np

from agents.agent import Agent
from utilities import operators
from utilities import preferences
from utilities import results

tests = 100
iteration_limit = 10000

mode = "symmetric" # ["symmetric" | "asymmetric"]
evidence_only = False
demo_mode = True

evidence_rate = 10/100

noise_values = [-10.0, -5.0, -1.0, -0.1, 0.0, 1.0, 5.0, 10.0, 20.0, 100.0]
noise_value = None   # None

comparison_errors = []

# Set the initialisation function for agent preferences: [uniform, other].
init_preferences = preferences.ignorant_pref_generator

# Output variables
directory = "../results/test_results/pddm/"
file_name_params = []

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
    # evidential updating.
    reached_convergence = True
    for agent in agents:
        # Currently, just testing with random evidence.
        evidence = preferences.random_evidence(
            states,
            noise_value,
            comparison_errors,
            random_instance
        )

        # print(agent.preferences)

        if random_instance.random() <= evidence_rate:
            agent.evidential_updating(operators.combine(agent.preferences, evidence))

        reached_convergence &= agent.steady_state()

    if reached_convergence:
        return False
    elif evidence_only:
        return True

    # Agents then combine at random

    # Symmetric
    if mode == "symmetric":
        agent1 = agents[random.randint(0,len(agents) - 1)]
        agent2 = agent1
        while agent2 == agent1:
            agent2 = agents[random.randint(0,len(agents) - 1)]

        new_preference = operators.combine(agent1.preferences, agent2.preferences)
        # print(new_preference)
        # Symmetric, so both agents adopt the combination preference.
        agent1.update_preferences(new_preference)
        agent2.update_preferences(new_preference)

    # Asymmetric
    # if mode == "asymmetric":

    return True


def main():
    """
    Main function for simulation experiments. Allows us to initiate start-up
    separately from main loop, and to extract results from the main loop at
    request. For example, the main_loop() will return TRUE when agents have
    fully converged according to no. of iterations unchanged. Alternatively,
    data can be processed for each iteration, or each test.
    """

    # Parse the arguments of the program, e.g., agents, states, random init.
    parser = argparse.ArgumentParser(description="Preference-based distributed\
    decision-making in a multi-agent environment.")
    parser.add_argument("agents", type=int)
    parser.add_argument("states", type=int)
    parser.add_argument("-r", "--random", type=bool, help="Random seeding of the RNG.")
    arguments = parser.parse_args()

    global comparison_errors
    global noise_value

    if noise_value is not None:
        for state in range(1, arguments.states):
            comparison_errors.append(preferences.comparison_error(
                state / arguments.states,
                noise_value
            ))

    random_instance = random.Random()
    # This needs to be fixed using GETSTATE and SETSTATE
    random_instance.seed(128) if arguments.random == None else random_instance.seed()

    # Set up the collecting of results
    preference_results = [
        [
            [0.0 for x in range(arguments.states)] for y in range(tests)
        ] for z in range(iteration_limit + 1)
    ]
    preference_results = np.array(preference_results)

    # Repeat the setup and loop for the number of simulation runs required
    max_iteration = 0
    for test in range(tests):
        print("Test #" + str(test), end="\r")
        agents = list()
        # Create an instance of a RNG that is either seeded for consistency of simulation
        # results, or create using a random seed for further testing.

        # Initial setup of agents and environment.
        setup(arguments.agents, arguments.states, agents, random_instance)

        # Pre-loop results based on agent initialisation.
        for agent in agents:
            prefs = agent.identify_preference()
            for pref in prefs:
                preference_results[0][test][pref] += 1.0 / len(prefs)

        # Main loop of the experiments. Starts at 1 because we have recorded the agents'
        # initial state above, at the "0th" index.
        for iteration in range(1, iteration_limit + 1):
            if main_loop(agents, arguments.states, mode, random_instance):
                for agent in agents:
                    prefs = agent.identify_preference()
                    for pref in prefs:
                        preference_results[iteration][test][pref] += 1.0 / len(prefs)
            # If the simulation has converged, end the test.
            else:
                print("Converged: ", iteration)
                max_iteration = iteration if iteration > max_iteration else max_iteration
                for agent in agents:
                    prefs = agent.identify_preference()
                    for pref in prefs:
                        preference_results[iteration][test][pref] += 1.0 / len(prefs)
                # print(iteration)
                for iter in range(iteration + 1, iteration_limit + 1):
                    # if iter == iteration + 1:
                        # print(iter, iteration_limit)
                    preference_results[iter][test] = np.copy(preference_results[iteration][test])
                break

    # Post-loop results processing (normalisation).
    preference_results /= len(agents)

    # Recording of results.
    # First, add parameters in sequence.
    global directory
    global file_name_params
    directory += "{0}/{1}/".format(arguments.agents, arguments.states)
    file_name_params.append("{:.3f}".format(evidence_rate))
    file_name_params.append("er")
    if noise_value is not None:
        file_name_params.append("{:.3f}".format(noise_value))
        file_name_params.append("nv")
    # Then write the results given the parameters.
    results.write_to_file(
        directory,
        "preferences",
        file_name_params,
        preference_results,
        max_iteration
    )

    # if demo_mode:
        # Output plots while running simulations, but do not record the results.
    # else:
        # Record the results but skip the plotting.


    sys.exit(1)


if __name__ == "__main__":
    main()

