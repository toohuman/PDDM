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
    closure = set([(rows[i], columns[i]) for i in range(len(rows))])

    # Source: https://stackoverflow.com/questions/8673482/transitive-closure-python-tuples
    # Form the transitive closure
    while True:
        new_relations = set((w,x) for x,y in closure for q,w in closure if q == y)
        # Form the union of the new relations with the current closure
        closure_until_now = closure | new_relations

        if closure_until_now == closure:
            break

        closure = closure_until_now

    print(closure)

    return closure

# Identify and remove cycles in the graph