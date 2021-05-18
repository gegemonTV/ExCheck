from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome_page():
    return render_template("welcome_page/index.html")


@app.route('/generate')
def generate_page():
    return render_template("generate_page/index.html")


@app.route('/submit')
def submit_page():
    return render_template("submit_page/index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 64209, True)

