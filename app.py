from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
@app.get("/home")
def index():
    return render_template("index.html", title="Home")

@app.get("/add")
@app.post("/add")
def add_habit():

    return render_template("add.html", title="Add Habit")
