from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def read():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.new_user(data)
    return redirect("/")

@app.route("/users/<int:user_id>")
def display_user(user_id):
    data = {
        "id" : user_id
    }
    user = User.show_user(data)
    return render_template("info.html", user = user)

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    data = {
        "id": user_id
    }
    user = User.show_user(data)
    return render_template('edit.html', user_id = user_id, user = user)

@app.route("/users/<int:user_id>/update", methods=["POST"])
def update(user_id):
    data = {
        "id": user_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }
    user = User.update(data)
    return redirect(f"/users/{user_id}")

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)