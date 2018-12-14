import numpy as np

def uniform_pref_generator(states, rand):
    """ Create a matrix of n x n zeros: a uniform, "unknown" preference. """

    # Set the preferences to all unknowns (0)
    preferences =  np.zeros((states, states), int)
    # Set the diagonals to false (-1)
    for x in range(states):
        preferences[x][x] = -1

    return preferences