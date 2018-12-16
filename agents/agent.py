class Agent:

    preferences = None
    interactions = int

    def __init__(self, preferences):

        self.preferences = preferences
        self.interactions = 0


    def evidential_updating(self, preferences):

        self.preferences = preferences


    def update_preferences(self, preferences):

        self.preferences = preferences
        self.interactions += 1

