import email
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Hello!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    sport = db.Column("sport", db.String(100))
    calorie_intake = db.Column("calorie", db.Integer)
    sleep  = db.Column("sleep", db.Integer)
    recovery = db.Column("recovery", db.Integer)

    def __init__(self, calorie_intake, sleep, recovery):
        self.calorie_intake = calorie_intake
        self.sleep = sleep
        self.recovery = recovery


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
