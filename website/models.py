from collections import UserList
from time import timezone
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

class User(db.Model, UserMixin):    
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    active = db.Column(db.Boolean)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)

    access = db.Column(db.Integer, nullable=False) 
    team = db.Column(db.String(150))

    branch = db.Column(db.String(150)) 

    def __init__(self, email, password, first_name, last_name, access, branch, team):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.access = access
        self.branch = branch
        self.team = team

