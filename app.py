from flask import Flask, render_template, flash, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hello " + str(request.form['name_input']) + ". Nice to meet you!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
