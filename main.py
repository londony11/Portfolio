from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

RECIPIENTS = os.environ.get("RECIPIENTS")
MY_EMAIL = os.environ.get("MY_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY")
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


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = "Want to get in touch? Fill out the form below to send me a message, " \
              "and I will get back to you as soon as possible!"
    if request.method == "POST":
        email = f'Name: {request.form["name"]}\n' \
                f'Email: {request.form["email"]}\n' \
                f'Subject: {request.form["subject"]}\n' \
                f'Message:\n\n{request.form["message"]}'
        msg = MIMEMultipart()
        msg["From"] = MY_EMAIL
        msg["To"] = RECIPIENTS[0]
        msg["Subject"] = "Portfolio contact email"
        msg.attach(MIMEText(email, "plain"))
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENTS,
                msg=msg.as_string(),
            )
        message = "Successfully sent your message."
    return render_template("contact.html", message=message)


if __name__ == "__main__":
    app.run(debug=False, port=8080)
