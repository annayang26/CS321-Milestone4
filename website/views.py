# views.py
# show route to different html files
from . import db
from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from urllib import request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def login_page():
    return render_template('login.html', user=current_user)

@views.route('/athlete')
@login_required
def athlete():
    # check if the user has access to the page
    if current_user.access == 0:
        return render_template('athlete.html', user=current_user)
    # if not, then return the user to their own home page
    flash("you don't have access to this page", category='error')
    return render_template('<user.access>.html', user=current_user)


@views.route('/coach')
@login_required
def coach():
    if current_user.access == 1:
        return render_template('coach.html', user=current_user)
    flash("you don't have access to this page", category='error')
    return render_template('<user.access>.html', user=current_user)

@views.route('/admin')
@login_required
def admin():
    if current_user.access == 2:
        return render_template('admin.html', user=current_user)
    flash("you don't have access to this page", category='error')
    return render_template('<user.access>.html', user=current_user)

@views.route('/superadmin')
@login_required
def superadmin():
    if current_user.access == 3:
        return render_template('superadmin.html', user=current_user)
    flash("you don't have access to this page", category='error')
    return render_template('<user.access>.html', user=current_user)

@views.route('/database')
@login_required
def database():
    if current_user.access == 3:
        users = User.query.all()
        return render_template('database.html', user=current_user, database=users)
    flash("you don't have access to this page", category='error')

@views.route('/report')
@login_required
def report():
    if current_user.access == 3:
        return render_template('report.html', user=current_user)
    flash("you don't have access to this page", category='error')

@views.route('/add')
@login_required
def add():
    if current_user.access == 3:
        return render_template('add.html', user=current_user)
    flash("you don't have access to this page", category='error')
