



class Game:
    def __init__(self, round_count, player_one, player_two):
        self.round_count = round_count
        self.result_1 = 0
        self.result_2 = 0
        self.player_one = player_one
        self.player_two = player_two




    def roll_all_dices(self, dice_list):
        result = 0
        for dice in dice_list:
            result += dice.roll()

        return result




    def play(self):
        for _ in range(self.round_count):
            self.result_1 += self.roll_all_dices(self.player_one.dice_list)
            self.result_2 += self.roll_all_dices(self.player_two.dice_list)
            self.compare_results(self.result_1, self.result_2)

    def compare_results(self, result_1, result_2):
        if result_1 > result_2:
            self.player_one.wins += 1
            self.player_two.loses += 1
            self.player_one.money += 10
            self.player_two.money -= 10
        elif result_2 > result_1:
            self.player_one.loses += 1
            self.player_two.wins += 1
            self.player_one.money -= 10
            self.player_two.money += 10





