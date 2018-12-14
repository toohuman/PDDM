import numpy as np

def uniform_pref_generator(states, rand):
    """ Create a matrix of n x n zeros: a uniform, "unknown" preference. """

    return np.zeros((states, states), int)