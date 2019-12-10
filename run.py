from game import Game
from dice import Dice




def list_creator(dices_amount, dice_size):
    dices = []

    for counter in range(dices_amount):
        dice = Dice(dice_size)
        dices.append(dice)
    return dices

if __name__ == '__main__':

    dice_list_one = list_creator(5, 6)
    dice_list_two = list_creator(5, 6)

    game = Game(10, dice_list_one, dice_list_two)
    game.play()
    print(game.result_1)
    print(game.result_2)






