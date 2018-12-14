import numpy as np

def combine(prefs1, prefs2):

    preferences = np.add(prefs1, prefs2)
    for x in range(len(preferences)):
        preferences[x][x] = -1

    # Normalising extreme values: 2, -2.
    for i in range(len(preferences)):
        for j in range(len(preferences[i])):
            if preferences[i][j] == 2:
                preferences[i][j] = 1
            elif preferences[i][j] == -2:
                preferences[i][j] = -1

    return preferences

def transitive_closure(matrix):
