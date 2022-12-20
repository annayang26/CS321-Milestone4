import os
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from flask import Blueprint, render_template, request, flash, redirect, session, url_for, jsonify
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

plt.style.use(['seaborn-colorblind', 'seaborn-darkgrid'])
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'figure.figsize': [8,8]})

np.set_printoptions(suppress=True, precision=5)

auth = Blueprint('auth', __name__ )

Emails = []

SuperAminList = []
AthleteList = []

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login successfully!', category='success')
                login_user(user, remember=True)
                          
                if user.access == 3:
                    return redirect(url_for('views.superadmin'))
                elif user.access == 2:
                    return redirect(url_for('views.peak'))
                elif user.access == 1:
                    return redirect(url_for('views.coach'))
                else:
                    return redirect(url_for('views.athlete'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. Please sign up or contact PEAK team.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods= ['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
            return redirect(url_for('auth.login'))
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        else:
            if email == "superadmin@colby.edu":
                access = 3
            elif email == "admin1@colby.edu":
                access = 2
            elif email == "coach@colby.edu":
                access = 1
            else:
                access = 0
            new_user = User(email=email, first_name=first_name, last_name = last_name, access=access, \
                            password=generate_password_hash(password1, method='sha256'), branch=None, team=None)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            if new_user.access == 3:
                return redirect(url_for('views.superadmin'))
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)

@auth.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name'] 
        role = request.form.get('role')
        if role == "admin":
            branch = request.form.get('branch')
            team = branch
        else:
            team = request.form['team']
            branch = team 

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
            return redirect(url_for('views.add'))
        else:
            if role == "admin":
                access = 2
            elif role == "coach":
                access = 1
            else:
                access = 0
            password1 = '1111111'
            new_user = User(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            access=access,
                            password=generate_password_hash(password1, method='sha256'),
                            branch=branch, 
                            team=team)
            db.session.add(new_user)
            flash('The user is added successfully!', category='success')
            db.session.commit()

        return redirect(url_for('views.add'))

@auth.route('/upload', methods=('GET', 'POST'))
def upload():
    flash(request.method)
    if request.method == 'POST':
        sleep_data_df = pd.read_csv("website/data/sleep.csv")
        return render_template('upload.html',tables=[sleep_data_df.to_html()],titles=[''], user=current_user)
    else:
        sleep_data_df = None
    return render_template("upload.html", user=current_user, sleepData=sleep_data_df)
    
@auth.route('/edit/<int:user_id>', methods=('GET', 'POST'))
def edit(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        role = request.form.get('role')
        if user.access == 2:
            branch = request.form['branch']
            user.branch = branch
        else: 
            team = request.form['team']
            user.team = team

        user.first_name = first_name
        user.last_name = last_name
        user.email = email 

        if role == "admin":
            user.access = 2
        elif role == "coach":
            user.access = 1
        else:
            user.access = 2

        db.session.add(user)
        db.session.commit()

        flash('The user information has been changed', category='success')

        return redirect(url_for('auth.edit', current_user=current_user, user_id=user.id))
    return render_template('edit.html', user=current_user, edit_user=user)

