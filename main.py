import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 'Hello and welcome to the HarpNet API revision 3.0 </p>'


@app.route('/game/check/pubtoken', methods=['GET'])  # Why do we even have this?
def check_pubtoken():
    game_id = request.args.get('id')  # Get game ID | 1 = Carmine
    pubtoken = request.args.get('token')

    default_response = jsonify(
        status=69,
        message='Default option - Public token not specified or invalid'
    )

    carmine_response = jsonify(
        status=0,
        message='Public token is valid',
        username='test',
        public='test'
    )

    if game_id == "1":
        return carmine_response

    return default_response


@app.route('/game/get/tags', methods=['GET'])
def get_tags():
    game_id = request.args.get('id')  # Get game ID | 1 = Carmine
    username = request.args.get('name')

    default_response = jsonify(
        status=69,
        message='Default option - game ID or username not specified or invalid'
    )

    carmine_response = jsonify(
        status=0,
        message="HNAPIv3",
        tags=[{'tag': 'speedy boi', 'color': "piss yellow"}]
    )

    if game_id == "1" and username:
        return carmine_response

    return default_response


@app.route('/game/get/userinfo', methods=['GET'])  # This is dumb and legacy, please fix
def get_userinfo():
    game_id = request.args.get('id')  # Get game ID | 1 = Carmine

    default_response = jsonify(
        status=69,
        message='Default option - game ID not specified or invalid'
    )

    carmine_response = jsonify(
        status=0,
        message="HNAPIv3",
        username="test",
        public="tits"
    )

    if game_id == "1":
        return carmine_response

    return default_response


@app.route('/game/get/user', methods=['GET'])  # This is dumb and legacy, please fix
def get_user():
    game_id = request.args.get('id')  # Get game ID | 1 = Carmine
    token = request.args.get('token')

    default_response = jsonify(
        status=69,
        message='Default option - game ID not specified or invalid'
    )

    carmine_response = jsonify(
        status=0,
        message="HNAPIv3",
        username="test",
        public="tits"
    )

    if game_id == "1":
        return carmine_response

    return default_response

# We're entering undocumented waters boys - wish me luck
#@app.route('/game/get/user', methods=['GET'])  # This is dumb and legacy, please fix
#def get_user():
#    return

app.run(port=80)
