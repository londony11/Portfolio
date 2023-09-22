from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "secret"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/project")
def project():
    return render_template("work-single.html")


if __name__ == "__main__":
    app.run(debug=True)
