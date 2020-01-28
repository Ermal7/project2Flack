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
    if session.get("user") is None:
        session["user"]=[]


    return render_template("index.html", notes=session["notes"])



if __name__ == '__main__':
    socketio.run(app)
