from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def home():
    return 'Hello and welcome to the HarpNet API revision 3.0 </p>'


@app.route('/game/check/pubtoken')  # Why do we even have this?
def check_pubtoken(id, token):

    default_response = {
        "status": 69,
        "message": 'Default option - Public token not specified or invalid'
    }

    carmine_response = {
        "status": 0,
        "message": 'Public token is valid',
        "username": 'test',
        "public": 'test'
    }

    if id == "1":
        return carmine_response

    return default_response


@app.get('/game/get/tags')
def get_tags(id, name):

    default_response = {
        "status": 69,
        "message": 'Default option - game ID or username not specified or invalid'
    }

    carmine_response = {
        "status": 0,
        "message": "HNAPIv3",
        "tags": [{'tag': 'speedy boi', 'color': "piss yellow"}]
    }

    if id == "1" and name:
        return carmine_response

    return default_response


@app.get('/game/get/userinfo')  # This is dumb and legacy, please  fix
def get_userinfo(id):

    default_response = {
        "status": 69,
        "message": 'Default option - game ID not specified or invalid'
    }

    carmine_response = {
        "status": 0,
        "message": "HNAPIv3",
        "username": "test",
        "public": "tits"
    }

    if id == "1":
        return carmine_response

    return default_response


@app.get('/game/get/user')  # This is dumb and legacy, please fix
def get_user(id, token):

    default_response = {
        "status": 69,
        "message": 'Default option - game ID not specified or invalid'
    }    

    carmine_response = {
        "status": 0,
        "message": "HNAPIv3",
        "username": "test",
        "public": "tits"
    }

    if id == "1":
        return carmine_response

    return default_response

# We're entering undocumented waters boys - wish me luck
#@app.route('/game/get/user', methods=['GET'])  # This is dumb and legacy, please fix
#def get_user():
#    return


