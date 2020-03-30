from flask import Flask, render_template, request
from dice import Dice
from gbl_const import handled_servers
from models.user import User
from player import Player
from game import Game
from validators.validator import validate_return_json

appl = Flask(__name__, template_folder='')

@appl.route('/return_results', methods = ['POST'])
def home():
    dice_one = []
    for dimension in request.json['diceListOne']:
            dice_one.append(Dice(dimension))
    dice_two = []
    for dimension in request.json['diceListTwo']:
        dice_two.append(Dice(dimension))
    dice_list_one = dice_one
    dice_list_two = dice_two


    player_one = Player(request.json['playerOneMoney'], dice_list_one)
    player_two = Player(request.json['playerTwoMoney'], dice_list_two)



    game = Game(request.json['roundCount'], player_one, player_two)
    game.play()
    result_1 = game.result_1
    result_2 = game.result_2
    round_count = game.round_count
    player_one_money = player_one.money
    player_two_money = player_two.money
    json = {}
    json['playerOneResult'] = result_1
    json['playerTwoResult'] = result_2
    json['playerOneMoney'] = player_one_money
    json['playerTwoMoney'] = player_two_money
    return json, 201

@appl.route('/create_user', methods = ['POST'])
def create_user():
    json = request.json
    print(json)
    return json

@appl.route('/user', methods = ['POST'])
def return_json():
    result = validate_return_json(request)
    if result is not None:
        print(result)
        return result
    user = User()
    user.from_json(request.json)
    user.first_name = 'lukasz'
    return user.to_json()

@appl.route('/index')
def index():
    identity = 'Tomek'
    return render_template('index.html', name = identity)

@appl.route('/')
def return_string():
    name = 'Tomek'
    return name

@appl.route('/send', methods = ['POST'])
def send():
    print(request.data)
    print(request.json)
    print(request.json['roundCount'])
    return {}, 200



if __name__ == '__main__':
    appl.run(debug=True)













