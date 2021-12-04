class Stats():
    """stats game"""

    def __init__(self):
        """init stats"""
        self.reset_stats()

    def reset_stats(self):
        self.lifes_left = 3
        self.score = 0