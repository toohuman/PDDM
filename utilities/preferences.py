import numpy as np

def ignorant_pref_generator(states):
    """ Create a matrix of n x n zeros: a uniform, "unknown" preference. """

    # Set the preferences to all unknowns (0).
    preferences =  np.zeros((states, states), int)
    # Set the diagonals to false (-1).
    for x in range(states):
        preferences[x][x] = -1

    return preferences

def random_evidence(states, random_instance):
    """ """

    evidence = np.zeros((states, states), int)
    index_i = random_instance.randint(0, states - 1)
    index_j = index_i
    while index_j == index_i:
        index_j = random_instance.randint(0, states - 1)

    if index_i < index_j:
        evidence[index_i][index_j] = -1
        evidence[index_j][index_i] = 1
    else:
        evidence[index_i][index_j] = 1
        evidence[index_j][index_i] = -1

    return evidence