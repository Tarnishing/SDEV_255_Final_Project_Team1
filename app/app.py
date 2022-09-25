from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
from flask_session import Session
from uuid import uuid4

app = Flask(__name__)
#  This generates a randomized string for the secret key.
app.config['SECRET_KEY'] = uuid4().hex

#  The session is set to permanent. This means that the session cookies won’t expire when the browser closes.
app.config['SESSION_PERMANENT'] = True
#  The session type is set to the filesystem, which means that the cookies are going to be stored locally on the server-side.
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

socketio = SocketIO(app)

def generate_game():
    return render_template('game.html')

#  The user socket ID is stored in the sesion when the use first connects to the page. The user socket ID is stored on the session variable sid.
@socketio.on('connect')
def connect():
    session['sid'] = request.sid

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        return generate_game()
    return render_template('index.html')