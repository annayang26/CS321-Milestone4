from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from . import db 
from datetime import datetime, timedelta
import os
import pandas as pd
import json
import plotly
import plotly.express as px
from .nutritiondonut import nutpie
from .sleeppiechart import sleeppie
from .recoverydonut import recpie
from . import gcal_utils as gcal
import google_auth_oauthlib.flow
import google.auth.transport.requests
import google.oauth2.credentials
import googleapiclient.discovery

views = Blueprint('views', __name__)

@views.route('/')
def login_page():
    return render_template('login.html', user=current_user)

@views.route('/athlete')
@login_required
def athlete():
    nutfig = nutpie('website/data/nutrition.csv', 2000)
    nutfigJSON = json.dumps(nutfig, cls=plotly.utils.PlotlyJSONEncoder)
    sleepfig = sleeppie('website/data/sleep.csv', 10)
    sleepfigJSON = json.dumps(sleepfig, cls=plotly.utils.PlotlyJSONEncoder)
    recfig = recpie('website/data/physiological cycles.csv', 10)
    recfigJSON = json.dumps(recfig, cls=plotly.utils.PlotlyJSONEncoder)
    if current_user.access == 0:
        return render_template('athlete.html', user=current_user, 
            nutfigJSON = nutfigJSON, 
            sleepfigJSON=sleepfigJSON, 
            recfigJSON=recfigJSON)
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
    nutfig = nutpie('website/data/nutrition.csv', 2000)
    nutfigJSON = json.dumps(nutfig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('calories.html', user=current_user,
                nutfigJSON=nutfigJSON)

GCAL_OAUTH_SCOPES = ['https://www.googleapis.com/auth/calendar']
GCAL_SECRETS_FILE = 'oauth_credentials.json'
REDIRECT_URI = 'http://localhost:5000/oauth2callback'

in_heroku = os.environ.get('IN_HEROKU', None)
if in_heroku:
    JSON = os.environ.get('GOOGLE_CREDENTIALS')
    GCAL_SECRETS_FILE = json.loads(JSON)
    base = os.environ.get('PORT')
    red_uri = base + 'oauth2callback'
    REDIRECT_URI = red_uri


@views.route('/gcal_authorize')
def gcal_authorize():
    print(type(GCAL_SECRETS_FILE))
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        GCAL_SECRETS_FILE, scopes=GCAL_OAUTH_SCOPES)

    flow.redirect_uri = REDIRECT_URI

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        prompt='consent',
        include_granted_scopes='true')

    session['state'] = state

    return redirect(authorization_url)



@views.route('/oauth2callback')
def gcal_oauth2callback():
    state = session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        GCAL_SECRETS_FILE, scopes=GCAL_OAUTH_SCOPES, state=state)
    flow.redirect_uri = REDIRECT_URI
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    return redirect('/calendar')


@views.route('/calendar')
@login_required
def calendar():
    if 'credentials' not in session:
        return redirect('/gcal_authorize')

    credentials = google.oauth2.credentials.Credentials(
        **session['credentials'])

    calendar_service = googleapiclient.discovery.build(
        'calendar', 'v3', credentials=credentials)
    
    events = gcal.view_event(calendar_service)

    session['credentials'] = credentials_to_dict(credentials)

    return render_template('calendar.html', user=current_user, list_of_events=events)

@views.route('/create-event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        event_name = request.form['event-name']
        event_description = request.form['event-description']
        event_location = request.form['event-location']
        event_start_date = request.form['event-start-date']
        event_start_time = request.form['event-start-time']
        event_end_date = request.form['event-end-date']
        event_end_time = request.form['event-end-time']

        credentials = google.oauth2.credentials.Credentials(
            **session['credentials'])
        calendar_service = googleapiclient.discovery.build(
            'calendar', 'v3', credentials=credentials)

        starttime = event_start_date + 'T' + event_start_time + ':00'
        endtime = event_end_date + 'T' + event_end_time + ':00'

        event = {
            'summary': event_name,
            'location': event_location,
            'description': event_description,
            'start': {
                'dateTime': starttime,
                'timeZone': 'America/New_York',
            },
            'end': {
                'dateTime': endtime,
                'timeZone': 'America/New_York',
            },
            'attendees': [
                None,
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
            }

        event = calendar_service.events().insert(calendarId='primary', body=event).execute()

        return redirect(url_for('views.calendar'))

def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}
