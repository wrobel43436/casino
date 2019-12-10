from random import randrange



class Dice:

    def __init__(self, positions):
        self.positions = positions
        self.last_roll = 0

    def roll(self):
        self.last_roll = randrange(1, self.positions)
        return self.last_roll




