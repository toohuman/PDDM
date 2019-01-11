import math
import numpy as np

def ignorant_pref_generator(states):
    """ Create a matrix of n x n zeros: a uniform, "unknown" preference. """

    # Set the preferences to all unknowns (0).
    preferences =  np.zeros((states, states), int)
    # Set the diagonals to false (-1).
    np.fill_diagonal(preferences, -1)

    return preferences

# /**
#  * Generate the error function for calculating probabilities of
#  * confusing one option for an alternative, depending on their
#  * relative placement to one another.
#  */
# auto comparisonError(const double x, const double lambda)
# {
#     import std.math : E;
#     import std.math : pow;

#     // Bound the error function in [0, bound]
#     immutable auto bound = 0.5;

#     if (lambda == 0) return bound * (1 - x);

#     immutable double errorValue = ( pow(E, -lambda * x) - pow(E, -lambda) )
#                                 / ( 1.0 - pow(E, -lambda) );

#     return bound * errorValue;
# }
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


def random_evidence(states, random_instance):
    """ Generate a random piece of evidence. """

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