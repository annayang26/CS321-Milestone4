from __future__ import print_function

from datetime import datetime, timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from apiclient.discovery import build
from googleapiclient.errors import HttpError


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
            event_list.append(time_list[0])
            time = time_list[1].split("-")
            event_list.append(time[0])
            title = event['summary']
            event_list.append(title)
            list_of_events.append(event_list)

        return list_of_events
        
    except HttpError as error:
        print('An error occurred: %s' % error)