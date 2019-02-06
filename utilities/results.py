# This file contains the functions for calculating results from the agents'
# preferences, as well as writing the results to a file.

import numpy as np

def identify_preference(preferences):
    """
    """

    max_pref = 0
    preference = []
    for i, row in enumerate(preferences):
        count = np.count_nonzero(row == 1)
        if count > max_pref:
            max_pref = count
            preference = [i]
        elif count == max_pref:
            preference.append(i)

    return sorted(preference)


def loss(preferences, true_preferences, normalised = True):
    """
    Named after a loss function in machine learning, this function calculates
    the sum of the differences of two matrices, scaled by 0.5 so that we count
    half-values for having no preference between two elements.
    The idea is that we compare the agent's preferences with the true state of
    the world and a return value of 0 indicates no differences (100% similarity)
    or "zero loss" between the true value and the agents' preferences.

    The normalisation option uses the worst possible preference (in relation to
    the true state of the world) to normalise the values in [0, 1].
    """

    differences = np.subtract(preferences, true_preferences)
    differences = np.absolute(differences)

    if normalised:
        normaliser = loss(true_preferences, np.transpose(true_preferences), False)
        return np.sum(np.multiply(differences, 0.5)) / normaliser

    return np.sum(np.multiply(differences, 0.5))


def quality(preferences, true_preferences, normalised = True):
    """
    Defined as the loss function, but where we compare an agent's preferences
    with the opposite of the true state of the world, so that we get a "quality
    value" where the higher the score, the more accurate the agent's preferences.
    This value can be normalised.
    """

    return loss(preferences, np.transpose(true_preferences), normalised)


def write_to_file(directory, file_name, params, data, max, array_data = False):
    """
    """

    with open(directory + file_name + '_' + '_'.join(params) + '.csv', 'w') as file:
        for i, test_data in enumerate(data):
            for j, results_data in enumerate(test_data):
                if array_data:
                    file.write('[')
                    for k, sub_data in enumerate(results_data):
                        file.write('{:.4f}'.format(sub_data))
                        if k != len(results_data) - 1:
                            file.write(',')
                    file.write(']')
                else:
                    file.write('{:.4f}'.format(results_data))
                # Determine whether the line ends here
                if j != len(test_data) - 1:
                    file.write(',')
                else:
                    file.write('\n')
            if i > max:
                break