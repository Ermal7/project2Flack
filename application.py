import os

from flask import Flask,render_template, session,request
from flask_socketio import SocketIO, emit
from flask_session import Session
from models import *

#Socket IO
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

#Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

users = []
channels= []

@app.route("/",methods=["GET", "POST"])
def index():
    if session.get("current_channel") is None:
        session["current_channel"] = Channel("")

    if request.method == "GET":
        if session.get("display_name") is None:
            return render_template("register.html")
        else:
            return render_template("index.html",current_channel=session["current_channel"], user=session["display_name"], users=users, channels=channels)

    else:
        if session.get("display_name") is None:
            user = request.form.get("display_name")
            session["display_name"] = user
            users.append(user)
        return render_template("index.html", current_channel=session["current_channel"], user=session["display_name"], users=users, channels=channels)

@app.route("/select",methods=["POST"])
def select():
    session["current_channel"] = Channel(request.form.get("selected_channel"))
    return "success"


@socketio.on("add channel")
def vote(data):
    new_channel_name = data["channel_name"]
    for channel in channels:
        if channel.name == new_channel_name:
            return "channel exists"
    new_channel = Channel(new_channel_name)
    channels.append(new_channel)
    emit("append channel", {"new_channel": new_channel_name}, broadcast=True)
