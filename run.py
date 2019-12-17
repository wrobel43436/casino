from game import Game
from dice import Dice
from player import Player




def list_creator(dices_amount, dice_size):
    dices = []

    for _ in range(dices_amount):
        dice = Dice(dice_size)
        dices.append(dice)

    return dices

if __name__ == '__main__':

    dice_list_one = list_creator(5, 6)
    dice_list_two = list_creator(5, 6)


    player_one = Player(100, 0, 0, dice_list_one, key = 1)
    player_two = Player(200, 0, 0, dice_list_two,  key = 2)







    game = Game(10, player_one, player_two)
    game.play()

    print(game.result_1)
    print(game.result_2)
    print("player one wins " + str(player_one.wins))
    print("player one loses " + str(player_one.loses))
    print("player two wins " + str(player_two.wins))
    print("player two loses " + str(player_two.loses))






