from flask import Flask, render_template, request

app = Flask(__name__)
list_of_habits = list()


@app.get("/")
@app.get("/home")
def index():
    return render_template("index.html", title="Home", list_of_habits=list_of_habits)


@app.get("/add")
@app.post("/add")
def add_habit():
    if request.method == "POST":
        list_of_habits.append(request.form.get("habit"))
        print(list_of_habits)

    return render_template("add_habit.html", title="Add Habit")
