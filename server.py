from chess import Chess
from flask import Flask, render_template, redirect
import json

app = Flask(__name__)
chess = Chess()

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/join/")
@app.route("/join/<string:game_id>")
def join_game(game_id=None):
    if game_id == "24601":
        return render_template('game.html', game_id=game_id)
    else:
        return render_template('bad_game.html', game_id=game_id)

@app.route("/state/<string:game_id>")
def get_game_state(game_id=None):
    state = chess.get_state(game_id)
    response = json.dumps(state)
    return response

@app.route("/start/")
@app.route("/start/<string:ruleset>")
def start_game(ruleset=None):
    if ruleset == None:
        return render_template('bad_game.html', game_id=game_id)
    game_id = chess.start_game(named_ruleset=ruleset)
    # Temporary hack while we're abusing the game ID box for rulesets
    # Remove start method and merge with play once rulepicker is in place.
    return redirect(f'/play/{game_id}')

@app.route("/play/")
@app.route("/play/<string:game_id>")
def play_game(game_id=None):
    if game_id:
        return render_template('game.html', game_id=game_id)
    else:
        return render_template('bad_game.html', game_id=game_id)
