# views.py
# show route to different html files
# from . import db
# from .models import User
# from flask import Blueprint, render_template, request, flash, redirect, url_for
# from urllib import request
# from flask_login import login_required, current_user

# views = Blueprint('views', __name__)

from __future__ import print_function
from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from . import db 
from datetime import datetime, timedelta
import os.path
from .quickstart import *
import google.oauth2.credentials
import googleapiclient.discovery
import pandas as pd
import json
import plotly
import plotly.express as px
from .nutritiondonut import nutpie
from .sleeppiechart import sleeppie
from .recoverydonut import recpie

views = Blueprint('views', __name__)

@views.route('/')
def login_page():
    return render_template('login.html', user=current_user)

@views.route('/athlete')
@login_required
def athlete():
    nutfig = nutpie('website/data/Nutrition.csv', 2000)
    nutfigJSON = json.dumps(nutfig, cls=plotly.utils.PlotlyJSONEncoder)
    sleepfig = sleeppie('website/data/sleep.csv', 10)
    sleepfigJSON = json.dumps(sleepfig, cls=plotly.utils.PlotlyJSONEncoder)
    recfig = recpie('website/data/physiological cycles.csv', 10)
    recfigJSON = json.dumps(recfig, cls=plotly.utils.PlotlyJSONEncoder)
    # check if the user has access to the page
    if current_user.access == 0:
        return render_template('athlete.html', user=current_user, 
            nutfigJSON = nutfigJSON, 
            sleepfigJSON=sleepfigJSON, 
            recfigJSON=recfigJSON)
    # if not, then return the user to their own home page
    flash("you don't have access to this page", category='error')

@views.route('/coach-dashboard')
@login_required
def coach():
    if current_user.access == 1:
        return render_template('coach-dashboard.html', user=current_user)
    flash("you don't have access to this page", category='error')

@views.route('/peak')
@login_required
def peak():
    if current_user.access == 2:
        return render_template('peak.html', user=current_user)
    flash("you don't have access to this page", category='error')

@views.route('/admin_dashboard')
@login_required
def superadmin():
    if current_user.access == 3:
        return render_template('admin_dashboard.html', user=current_user)
    flash("you don't have access to this page", category='error')

@views.route('/database')
@login_required
def database():
    if current_user.access == 3:
        users = User.query.all()
        return render_template('database.html', user=current_user, database=users)
    flash("you don't have access to this page", category='error')

@views.route('/reportpage')
@login_required
def report():
    if current_user.access == 3:
        return render_template('reportchoose.html', user=current_user)
    flash("you don't have access to this page", category='error')

@views.route('/reportgen')
@login_required
def reports():
    if current_user.access == 3:
        return render_template('reportpage.html', user=current_user)
    flash("you don't have access to this page", category='error')

@views.route('/add')
@login_required
def add():
    if current_user.access == 3:
        return render_template('add.html', user=current_user)
    flash("you don't have access to this page", category='error')

@views.route('/teambreakdown')
@login_required
def team_breakdown():
    if current_user.access > 1:
        return render_template('teambreakdown.html', user=current_user)

@views.route('/breakdown')
@login_required
def athlete_breakdown():
    if current_user.access > 0:
        return render_template('breakdown.html', user=current_user)

@views.route('/sleep')
@login_required
def sleep_breakdown():
    # Attempting Sleep breakdown
    # sleep_csv = sleepcsv()
    # # with open(sleep_csv) as file:
    # reader = csv.reader(sleep_csv)
    # if current_user.access >= 0:
    #     return render_template('sleep.html', user=current_user,
    #         sleep_csv = reader)
    sleepfig = sleeppie('website/data/sleep.csv', 10)
    sleepfigJSON = json.dumps(sleepfig, cls=plotly.utils.PlotlyJSONEncoder)
    if current_user.access >= 0:
        return render_template('sleep.html', user=current_user, 
            sleepfigJSON=sleepfigJSON)

@views.route('/recovery')
@login_required
def recovery_breakdown():
    recfig = recpie('website/data/physiological cycles.csv', 10)
    recfigJSON = json.dumps(recfig, cls=plotly.utils.PlotlyJSONEncoder)
    if current_user.access >= 0:
        return render_template('recovery.html', user=current_user,
            recfigJSON=recfigJSON)

@views.route('/calories')
@login_required
def calories_breakdown():
    nutfig = nutpie('website/data/Nutrition.csv', 2000)
    nutfigJSON = json.dumps(nutfig, cls=plotly.utils.PlotlyJSONEncoder)
    if current_user.access >= 0:
        return render_template('calories.html', user=current_user,
            nutfigJSON=nutfigJSON)

@views.route('/calendar')
@login_required
def calendar():
    creds = get_cred()
    service = initialize_sheets(creds)
    events = view_event(service)
    print("hi")
    # create_event()
    return render_template('calendar.html', user=current_user, list_of_events=events)

@views.route('/create-event', methods=['GET', 'POST'])
def create_event():
    # Get form data
    if request.method == 'POST':
        event_name = request.form['event-name']
        event_description = request.form['event-description']
        event_location = request.form['event-location']
        event_start_date = request.form['event-start-date']
        event_start_time = request.form['event-start-time']
        event_end_date = request.form['event-end-date']
        event_end_time = request.form['event-end-time']

        # print(event_name)

        cred = get_cred()
        service = initialize_sheets(cred)

        starttime = event_start_date + 'T' + event_start_time + ':00'
        endtime = event_end_date + 'T' + event_end_time + ':00'

        add_event(service, event_name, starttime, endtime, 'America/New_York', None, None, None)

        # return render_template('calendar.html', user=current_user)
        return redirect(url_for('views.calendar'))
