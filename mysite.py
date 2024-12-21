from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {
        "link": "Перейти на главную страницу"
    }
    return render_template("home_account.html", **context)

@app.route("/about.html")
def about():
    context = {
        "link": "О нас"
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()