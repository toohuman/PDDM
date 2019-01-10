import numpy as np

def combine(prefs1, prefs2):
    """
    A renormalised sum of the two preference matrices.
    """

    preferences = np.add(prefs1, prefs2)
    # Ensure diagonals remain false
    np.fill_diagonal(preferences, -1)
    # Normalising extreme values: 2, -2.
    np.clip(preferences, -1, 1, preferences)

    return preferences

def transitive_closure(matrix):
    """
    Form the transitive closure of the input matrix by filling in relations
    where they are missing.
    """

    # Identify the binary relations of states (p > q)
    rows, columns = np.where(matrix == 1)
    closure = set([(rows[i], columns[i]) for i in range(len(rows))])
    # Copy the initial closure of the preference matrix for comparison at the end
    initial_closure = closure.copy()

    # Identify the transitive relations
    # Source: https://stackoverflow.com/questions/8673482/transitive-closure-python-tuples
    while True:
        new_relations = set((x,w) for x,y in closure for q,w in closure if q == y)
        # Form the union of the new relations with the current closure
        closure_until_now = closure | new_relations

        if closure_until_now == closure:
            break

        closure = closure_until_now

    # Form the transitive closure
    for x,y in closure:
        matrix[x][y] = 1
        matrix[y][x] = -1

    return True if initial_closure == closure else False

# Identify and remove cycles in the graph
def destroy_cycles(matrix):
    """
    """
