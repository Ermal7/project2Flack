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
    if request.method == "GET":
        if session.get("display_name") is None:
            return render_template("register.html")
        else:
            return render_template("index.html", display_name=session["display_name"],display_names=display_names,channel_names=channel_names)

    else:
        if session.get("display_name") is None:
            display_name = request.form.get("display_name")
            session["display_name"]= display_name
            display_names.append(display_name)
            #printf(display_names)
        return render_template("index.html", display_name=session["display_name"],display_names=display_names,channel_names=channel_names)



@app.route("/create", methods=["POST"])
def create_channel():
    new_channel = request.form.get("channel_name")
    for channel in channel_names:
        if channel == new_channel:
            return "exists"
    channel_names.append(new_channel)
    return new_channel
