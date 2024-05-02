from flask import Flask, render_template, request #on importe ce que l'user a rempli dans la form

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/play")
def play():


    return render_template("play.html")