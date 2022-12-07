from __future__ import print_function

from datetime import datetime, timedelta
import os.path
# from flask import Flask, request
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from apiclient.discovery import build
from googleapiclient.errors import HttpError
# import googleapiclient.discovery

# app = Flask(__name__)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_cred():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds 

def initialize_sheets(creds):
    service = build('calendar', 'v3', credentials=creds)
    return service

def view_event(service):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    try:

        # Call the Calendar API
        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return None


        list_of_events = []
        # Prints the start and name of the next 10 events
        for event in events:
            event_list = []
            start = event['start'].get('dateTime', event['start'].get('date'))
            time_list = start.split("T")
            time_convert = datetime.strptime(time_list[0], "%Y-%m-%d")
            event_list.append(time_convert.strftime("%d %B %Y"))
            time = time_list[1].split("-")
            event_list.append(time[0])
            title = event['summary']
            event_list.append(title)
            list_of_events.append(event_list)

        return list_of_events
        
    except HttpError as error:
        print('An error occurred: %s' % error)

def add_event(service, subject, starttime, endtime, timeZone='America/New_York', 
              emails=None, location=None, description=None):
    try:

        event = {
            'summary': subject,
            'location': None,
            'description': None,
            'start': {
                'dateTime': starttime,
                'timeZone': timeZone,
            },
            'end': {
                'dateTime': endtime,
                'timeZone': timeZone,
            },
            'attendees': [
                emails,
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
            }

        event = service.events().insert(calendarId='primary', body=event).execute()

    except HttpError as error:
        print('An error occurred: %s' % error)

# @app.route('/create-event', methods=['POST'])
# def create_event():
#     # Get form data
#     event_name = request.form['event-name']
#     event_description = request.form['event-description']
#     event_location = request.form['event-location']
#     event_start_date = request.form['event-start-date']
#     event_start_time = request.form['event-start-time']
#     event_end_date = request.form['event-end-date']
#     event_end_time = request.form['event-end-time']

#     # Create event on Google Calendar using the form data
#     event = {
#         'summary': event_name,
#         'location': event_location,
#         'description': event_description,
#         'start': {
#             'dateTime': event_start_date + 'T' + event_start_time,
#             'timeZone': 'America/New_York',
#         },
#         'end': {
#             'dateTime': event_end_date + 'T' + event_end_time,
#             'timeZone': 'America/New_York',
#         }
#         # 'reminders': {
#         # 'useDefault': true
#         # }
#     }
#     return event['htmlLink']

if __name__ == '__main__':
    cred = get_cred()
    service = initialize_sheets(cred)
    subject = 'CS321-Meeting'
    start = datetime(2022, 12, 6, 20, 0, 0)
    starttime = start.strftime("%Y-%m-%dT%H:%M:%S")
    end = start + timedelta(hours=4)
    endtime = end.strftime("%Y-%m-%dT%H:%M:%S")
    timezone = 'US/Eastern'
    # add_event(service, subject, starttime, endtime, timezone)
    list = view_event(service)
    print(list)