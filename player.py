from person import Person





class Player:
    def __init__(self, money, dice_list, foreign_key = None, key = None, wins = 0, loses = 0):
        self.key = key
        self.foreign_key = foreign_key
        self.money = money
        self.wins = wins
        self.loses = loses
        self.dice_list = dice_list