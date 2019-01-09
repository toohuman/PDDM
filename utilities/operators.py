import numpy as np

def combine(prefs1, prefs2):
    """
    A renormalised sum of the two preference matrices.
    """

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
    """
    Form the transitive closure of the input matrix by filling in relations
    where they are missing.
    """

    matrix[1][0] = 1
    print(matrix)

    # Identify the binary relations of states (p > q)
    rows, columns = np.where(matrix == 1)
    closure = [(rows[i], columns[i]) for i in range(len(rows))]
    print(closure)

    # For each pair (p > q), identify q's
    pairs = [[second_pair for second_pair in closure \
            if second_pair[0] == first_pair[1]] for first_pair in closure]

    print(pairs)

    return

# Identify and remove cycles in the graph