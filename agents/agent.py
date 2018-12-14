class Agent:

    preferences = None
    interactions = int

    def __init__(self, preferences):

        print("Agent created.")
        self.preferences = preferences
        self.interactions = 0


    def update_preferences(self, preferences):

        self.preferences = preferences

