import os

from flask import Flask,render_template, session
from flask_socketio import SocketIO, emit
from flask_session import Session

#Socket IO
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

#Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

display_names=[]
channel_names=[]

@app.route("/")
def index():
    if session.get("username") is None:
        session["username"]=[]
        return render_template("index1.html")
    else:
        return render_template("index2.html",username=session["usernotes"])
