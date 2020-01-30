import os

from flask import Flask,render_template, session,request
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

@app.route("/",methods=["GET", "POST"])
def index():
    if session.get("current_channel") is None:
        session["current_channel"]= ""

    if request.method == "GET":
        if session.get("display_name") is None:
            return render_template("register.html")
        else:
            return render_template("index.html",selected_channel=session["current_channel"], display_name=session["display_name"], display_names=display_names, channel_names=channel_names)

    else:
        if session.get("display_name") is None:
            display_name = request.form.get("display_name")
            session["display_name"]= display_name
            display_names.append(display_name)
        return render_template("index.html", selected_channel=session["current_channel"], display_name=session["display_name"], display_names=display_names, channel_names=channel_names)

@app.route("/select",methods=["POST"])
def select():
    session["current_channel"] = request.form.get("selected_channel")
    return


@socketio.on("add channel")
def vote(data):
    new_channel = data["new_channel"]
    for channel in channel_names:
        if channel == new_channel:
            return
    channel_names.append(new_channel)
    emit("append channel", {"new_channel": new_channel}, broadcast=True)
