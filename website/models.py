# create user models 
# with different levels of access
from collections import UserList
from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)

    # user authentication information
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    # user information
    active = db.Column(db.Boolean)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)

    # determine access level
    access = db.Column(db.Integer, nullable=False) 
    team = db.Column(db.String(150))
    
    # for PEAK members only. 
    # 1: sports science
    # 2: strength and training
    # 3: sports medicine
    # 4: performance psychology
    # 5: nutrition
    branch = db.Column(db.Integer) 

    def __repr__(self):
        return f'<User {self.first_name}>'
    
    def allowed(self, access_level):
        return self.access >= access_level
    
    def get_access(self):
        return self.access

