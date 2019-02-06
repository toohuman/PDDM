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


def similarity(preferences, true_order):
    """
    """

    return


def write_to_file(directory, file_name, params, data, max):
    """
    """

    with open(directory + file_name + '_' + '_'.join(params) + '.csv', 'w') as file:
        for i, test_data in enumerate(data):
            for j, preferences in enumerate(test_data):
                file.write('[')
                for k, preference in enumerate(preferences):
                    file.write('{:.4f}'.format(preference))
                    if k != len(preferences) - 1:
                        file.write(',')
                file.write(']')
                if j != len(test_data) - 1:
                    file.write(',')
                else:
                    file.write('\n')
            if i > max:
                break