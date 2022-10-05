from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
from flask_session import Session
from uuid import uuid4
from save_load_manager import Save, Load

import pickle

app = Flask(__name__)
#  This generates a randomized string for the secret key.
app.config['SECRET_KEY'] = uuid4().hex

# The session is set to permanent. This means that the session cookies won’t expire when the browser closes.
# We need this to tore the user socket ID sid
app.config['SESSION_PERMANENT'] = True
# The session type is set to the filesystem, which means that the cookies are going to be stored locally on the server-side. .
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

socketio = SocketIO(app)

def generate_game():
    return render_template('game.html')

def generate_saved_game():
    load_manager = Load(".dat", "save_data")
    # Load values into game variables if save file exists
    items, room_num, progress = load_manager.load_game_data(["items", "room_num", "progress"], [[], 0, 0])
    return render_template('game.html')

# The user socket ID is stored in the sesion when the use first connects to the page. The user socket ID is stored on the session variable sid.
@socketio.on('connect')
def connect():
    session['sid'] = request.sid

# We accept GET and POST request from the / route
@app.route("/", methods = ['GET', 'POST'])
def index():
    # Render the game.html page if the PLAY button is clicked
    if request.method == 'POST':
        return generate_game()
    return render_template('index.html')

@app.route("/load", methods=['GET', 'POST'])
def load_game():
    if request.method == 'POST':
        return generate_saved_game()
    return render_template('index.html')