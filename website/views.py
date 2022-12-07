# views.py
# show route to different html files
# from . import db

from __future__ import print_function
from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from . import db 
from datetime import datetime, timedelta
import os.path

from . import gcal_utils as gcal
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import google.auth.transport.requests

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
    if current_user.access >= 0:
        return render_template('sleep.html', user=current_user)

@views.route('/recovery')
@login_required
def recovery_breakdown():
    if current_user.access >= 0:
        return render_template('recovery.html', user=current_user)

@views.route('/calories')
@login_required
def calories_breakdown():
    if current_user.access >= 0:
        return render_template('calories.html', user=current_user)


GCAL_OAUTH_SCOPES = ['https://www.googleapis.com/auth/calendar']
GCAL_SECRETS_FILE = 'oauth_credentials.json'
REDIRECT_URI = 'http://localhost:5000/oauth2callback'

@views.route('/gcal_authorize')
def gcal_authorize():
    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        GCAL_SECRETS_FILE, scopes=GCAL_OAUTH_SCOPES)

    # The URI created here must exactly match one of the authorized redirect URIs
    # for the OAuth 2.0 client, which you configured in the API Console. If this
    # value doesn't match an authorized URI, you will get a 'redirect_uri_mismatch'
    # error.
    flow.redirect_uri = REDIRECT_URI

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # approval_prompt='force',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    session['state'] = state

    return redirect(authorization_url)



@views.route('/oauth2callback')
def gcal_oauth2callback():
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    state = session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        GCAL_SECRETS_FILE, scopes=GCAL_OAUTH_SCOPES, state=state)
    flow.redirect_uri = REDIRECT_URI
    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    return redirect('/calendar')


@views.route('/calendar')
@login_required
def calendar():
    if 'credentials' not in session:
        return redirect('/gcal_authorize')

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **session['credentials'])

    calendar_service = googleapiclient.discovery.build(
        'calendar', 'v3', credentials=credentials)
    
    events = gcal.view_event(calendar_service)

    session['credentials'] = credentials_to_dict(credentials)

    return render_template('calendar.html', user=current_user, list_of_events=events)

def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}