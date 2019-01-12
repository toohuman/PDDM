import math
import numpy as np
import random

def ignorant_pref_generator(states):
    """ Create a matrix of n x n zeros: a uniform, "unknown" preference. """

    # Set the preferences to all unknowns (0).
    preferences =  np.zeros((states, states), int)
    # Set the diagonals to false (-1).
    np.fill_diagonal(preferences, -1)

    return preferences


def comparison_error(x: float, param: float):
    """
    Generate the error function for calculating probabilities of confusing
    one option for an alternative, depending on their relative placement
    to one another.
    """

    # Bound the error function in [0, bound]
    bound = 0.5

    # Special case:
    if param == 0.0:
        return (bound * (1 - x))

    error_value = ( pow(math.e, -param * x) - pow(math.e, -param) )\
                / ( 1.0 - pow(math.e, -param) )

    return bound * error_value


def random_evidence(states, noise_value, random_instance):
    """ Generate a random piece of evidence. """

    evidence = np.zeros((states, states), int)
    index_i = random_instance.randint(0, states - 1)
    index_j = index_i
    while index_j == index_i:
        index_j = random_instance.randint(0, states - 1)

    difference = abs(index_i - index_j) / states

    best_index = index_i if index_i > index_j else index_j
    worst_index = index_i if index_i < index_j else index_j

    if noise_value is None or \
        random_instance.random() > comparison_error(difference, noise_value):
        evidence[best_index][worst_index] = 1
        evidence[worst_index][best_index] = -1
    else:
        evidence[best_index][worst_index] = -1
        evidence[worst_index][best_index] = 1

    return evidence