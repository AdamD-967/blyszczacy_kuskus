from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "abc"

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

@app.route("/user")
def home():
    if "user" in session.values():
        return render_template("main.html")
    else:
        return render_template("no.html")

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect((url_for("login")))


if __name__ == "__main__":
    app.run(debug=True)
