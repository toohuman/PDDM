import numpy as np

from utilities import operators

class Agent:

    preferences     = None
    evidence        = int
    interactions    = int
    no_change       = bool
    since_change    = int

    def __init__(self, preferences):

        self.preferences = preferences
        self.interactions = 0
        self.evidence = 0
        self.no_change = True
        self.since_change = 0

    def update(self):

        if self.no_change:
            self.since_change += 1
        else:
            # CHECK THIS PART - IF CHANGE ONCE, THEN RESET THE COUNTER, BUT
            # NEXT UPDATE(), KEEP COUNTING
            self.no_change = True
            self.since_change = 0
            operators.transitive_closure(self.preferences)

    def evidential_updating(self, preferences):
        """
        Update the agent's preferences based on the evidence they received.
        Increment the evidence counter.
        """

        # Track the number of iterations
        if np.array_equal(preferences, self.preferences):
            self.no_change = True
        else:
            self.no_change = False

        self.preferences = preferences
        self.evidence += 1


    def update_preferences(self, preferences):
        """
        Update the agent's preferences based on having combined their preferences with
        those of another agent.
        Increment the interaction counter.
        """

        # Track the number of iterations
        if np.array_equal(preferences, self.preferences):
            self.no_change = True
        else:
            self.no_change = False

        self.preferences = preferences
        self.interactions += 1

