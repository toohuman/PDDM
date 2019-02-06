import numpy as np

from utilities import operators

class Agent:

    preferences     = None
    ordered_prefs   = []
    evidence        = int
    interactions    = int
    since_change    = int

    def __init__(self, preferences):

        self.preferences = preferences
        self.interactions = 0
        self.evidence = 0
        self.no_change = True
        self.since_change = 0

    def update(self):
        """
        Agent update method to be called after every belief update.
        """

        operators.transitive_closure(self.preferences)


    def steady_state(self, threshold):
        """ Check if agent has reached a steady state. """

        return True if self.since_change >= threshold else False



    def evidential_updating(self, preferences):
        """
        Update the agent's preferences based on the evidence they received.
        Increment the evidence counter.
        """

        # Track the number of iterations.
        if np.array_equal(preferences, self.preferences):
            self.since_change += 1
        else:
            self.since_change = 0

        self.preferences = preferences
        self.evidence += 1

        self.update()


    def update_preferences(self, preferences):
        """
        Update the agent's preferences based on having combined their preferences with
        those of another agent.
        Increment the interaction counter.
        """

        # Track the number of iterations.
        if np.array_equal(preferences, self.preferences):
            self.since_change += 1
        else:
            self.since_change = 0

        self.preferences = preferences
        self.interactions += 1

        self.update()

