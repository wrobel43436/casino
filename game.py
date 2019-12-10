



class Game:
    def __init__(self, round_count, dices_1, dices_2):
        self.round_count = round_count
        self.dices_1 = dices_1
        self.dices_2 = dices_2
        self.result_1 = 0
        self.result_2 = 0



    def roll_all_dices(self, dices):

        result = 0

        for dice in dices:
            result += dice.roll()

        return result





    def play(self):
        i = 0
        while i < self.round_count:
            self.result_1 += self.roll_all_dices(self.dices_1)
            self.result_2 += self.roll_all_dices(self.dices_2)
            i += 1







