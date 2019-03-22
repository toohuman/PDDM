import math
import random

# def ignorant_pref_generator(states):
#     """ Create a matrix of n x n zeros: a uniform, "unknown" preference. """

#     # Set the preferences to all unknowns (0).
#     preferences =  np.zeros((states, states), int)
#     # Set the diagonals to false (-1).
#     np.fill_diagonal(preferences, -1)

#     return preferences

def ignorant_pref_generator(states):
    """ Returns an empty set of preferences to denote complete uncertainty. """

    return set()

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
        return round(bound * (1 - x), 5)

    error_value = ( pow(math.e, -param * x) - pow(math.e, -param) )\
                / ( 1.0 - pow(math.e, -param) )

    return round(bound * error_value, 5)


# def random_evidence(states, noise_value, comparison_errors, random_instance):
#     """ Generate a random piece of evidence. """

#     evidence = np.zeros((states, states), int)
#     index_i = random_instance.randint(0, states - 1)
#     index_j = index_i
#     while index_j == index_i:
#         index_j = random_instance.randint(0, states - 1)

#     difference = abs(index_i - index_j) - 1
#     if noise_value is not None:
#         comp_error = comparison_errors[difference]

#     best_index = index_i if index_i > index_j else index_j
#     worst_index = index_i if index_i < index_j else index_j

#     if noise_value is None or random_instance.random() > comp_error:
#         evidence[best_index][worst_index] = 1
#         evidence[worst_index][best_index] = -1
#     else:
#         evidence[best_index][worst_index] = -1
#         evidence[worst_index][best_index] = 1

#     return evidence

def random_evidence(states, noise_value, comparison_errors, random_instance):
    """ Generate a random piece of evidence. """

    evidence = set()
    shuffled_states = [x for x in range(states)]
    random_instance.shuffle(shuffled_states)
    index_i = shuffled_states.pop()
    index_j = shuffled_states.pop()

    difference = abs(index_i - index_j) - 1
    if noise_value is not None:
        comp_error = comparison_errors[difference]

    best_index = index_i if index_i > index_j else index_j
    worst_index = index_i if index_i < index_j else index_j

    # if noise_value is None or random_instance.random() > comp_error:
    #     evidence[best_index][worst_index] = 1
    #     evidence[worst_index][best_index] = -1
    # else:
    #     evidence[best_index][worst_index] = -1
    #     evidence[worst_index][best_index] = 1

    if noise_value is None or random_instance.random() > comp_error:
        evidence.add((best_index, worst_index))
    else:
        evidence.add((worst_index, best_index))

    return evidence