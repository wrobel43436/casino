from person import Person





class Player:
    def __init__(self, money, wins, loses, dice_list, foreign_key = None, key = None):
        self.key = key
        self.foreign_key = foreign_key
        self.money = money
        self.wins = wins
        self.loses = loses
        self.dice_list = dice_list