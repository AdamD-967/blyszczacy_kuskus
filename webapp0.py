from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.secret_key = "abc"

db = SQLAlchemy(app)

class SampleData(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column(db.String(25))
    string = db.Column(db.String(25))

    def __init__(self, number, string):
        self.number = number
        self.string = string


@app.route("/view")
def view():
    return render_template("view.html", values=SampleData.query.all())

@app.route("/")
def start():
    return 'go to login page: <a href="/login">login</a>'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        out = request.form["ps"]
        session["user"] = out
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/user", methods=["GET", "POST"])
def home():
    if "user" in session.values():
        if request.method == "POST":
            num = request.form["num"]
            word = request.form["word"]
            data = SampleData(num, word)
            db.session.add(data)
            db.session.commit()
            return render_template("main.html")
        else:
            return render_template("main.html")
    else:
        return render_template("no.html")

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect((url_for("login")))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
