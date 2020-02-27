from flask import Flask
from dice import Dice
from player import Player
from game import Game

app = Flask(__name__)

@app.route('/')
def home():

    dice_one = Dice(6)
    dice_two = Dice(6)
    dice_list_one = [dice_one]
    dice_list_two = [dice_two]


    player_one = Player(100, 0 ,0, dice_list_one)
    player_two = Player(200, 0, 0, dice_list_two)

    game = Game(1, player_one, player_two)
    game.play()
    return str(game.result_1) + " " + str(game.result_2) +\
    ' ' + str(game.player_one.money) + ' ' + str(game.player_two.money)

    

if __name__ == '__main__':
    app.run(debug=True)













