# authentication
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user 

auth = Blueprint('auth', __name__ )

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
                if user.access == 0:
                    return redirect(url_for('views.athlete'))
                elif user.access == 1:
                    return redirect(url_for('views.coach'))
                elif user.access == 2:
                    return redirect(url_for('views.admin'))
                elif user.access == 3:
                    return redirect(url_for('views.superadmin'))
                else:
                    flash('User not in the system, please contact PEAK team if you think this is incorrect.', category='error')
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
            flash('Passwords don\'t match.', category='error')
        else:
            # add user to database
            # if the user email is this, make them the superadmin
            if email == "superadmin@colby.edu":
                access = 3
                # branch = 0
            elif email == "admin1@colby.edu":
                access = 2
                # branch = 0
            elif email == "coach@colby.edu":
                access = 1
                # branch = 0
            else:
                access = 0
                # branch = 0
            new_user = User(email=email, first_name=first_name, last_name = last_name, access=access, \
                            password=generate_password_hash(password1, method='sha256'), branch=0, team=None)
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

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
            return redirect(url_for('views.add'))
        else:
            if role == "athlete":
                access = 0
            elif role == "coach":
                access = 1
            elif role == "admin":
                access = 2
            password1 = '1111111'
            new_user = User(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            access=access,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            flash('The user is added successfully!', category='success')
            db.session.commit()

        return redirect(url_for('views.add'))

@auth.route('/<int:user_id>/edit/', methods=('GET', 'POST'))
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
        elif user.access == 1 or user.access == 0: 
            team = request.form['team']
            user.team = team

        user.first_name = first_name
        user.last_name = last_name
        user.email = email 

        if role == "athlete":
            user.access = 0
        elif role == "coach":
            user.access = 1
        elif role == "admin":
            user.access = 2

        db.session.add(user)
        db.session.commit()

        flash('The user information has been changed', category='success')

        return redirect(url_for('auth.edit', user_id=user.id))
    return render_template('edit.html', user=user)
