import numpy as np

def combine(prefs1, prefs2):

    preferences = np.add(prefs1, prefs2)
    for x in range(len(preferences)):
        preferences[x][x] = -1

    return preferences