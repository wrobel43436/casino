from flask import Flask, render_template
from dice import Dice
from player import Player
from game import Game

app = Flask(__name__, template_folder='')

@app.route('/return_results')
def home():

    dice_one = Dice(6)
    dice_two = Dice(6)
    dice_list_one = [dice_one]
    dice_list_two = [dice_two]


    player_one = Player(100, 0 ,0, dice_list_one)
    player_two = Player(200, 0, 0, dice_list_two)



    game = Game(2, player_one, player_two)
    game.play()
    result_1 = game.result_1
    result_2 = game.result_2
    round_count = game.round_count
    return render_template('return_results.html',
                           round_count = round_count,
                           result_one = result_1,
                           result_two = result_2)



@app.route('/index')
def index():
    identity = 'Tomek'
    return render_template('index.html', name = identity)





if __name__ == '__main__':
    app.run(debug=True)













