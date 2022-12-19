from website import create_app
import json
import pytest
from website import views
from website import gcal_utils as gcal
from flask import current_app

# app = create_app
# app.app_context().push()

def create_account_super(client):
    client.post("/sign-up",
                data={"email": "superadmin@colby.edu",
                      "firstname": "Super",
                      "lastname": "Admin",
                      "password1": "1111111",
                      "password2": "1111111"})

    client.post("/login",
                data={"email": "superadmin@colby.edu",
                        "password": "1111111"})

def create_account_peak(client):
    client.post("/sign-up",
                data={"email": "admin1@colby.edu",
                      "firstname": "Admin",
                      "lastname": "One",
                      "password1": "1111111",
                      "password2": "1111111"})

    client.post("/login",
                data={"email": "admin1@colby.edu",
                        "password": "1111111"})

def create_account_coach(client):
    client.post("/sign-up",
                data={"email": "coach@colby.edu",
                        "firstname": "Coach",
                        "lastname": "One",
                        "password1": "1111111",
                        "password2": "1111111"})

    client.post("/login",
                data={"email": "coach@colby.edu",
                        "password": "1111111"})


def create_account_athlete(client):
    client.post("/sign-up",
                data={"email": "athlete@colby.edu",
                        "firstname": "Athlete",
                        "lastname": "One",
                        "password1": "1111111",
                        "password2": "1111111"})

    client.post("/login",
                data={"email": "athlete@colby.edu",
                        "password": "1111111"})


def test_athlete_access(client):
    create_account_athlete(client)

    response = client.get('/sleep', follow_redirects=True)
    assert response.status_code == 200 # redirect to sleep breakdown

    response = client.get('/recovery', follow_redirects=True)
    assert response.status_code == 200 # redirect to recovery breakdown

    response = client.get('/calories', follow_redirects=True)
    assert response.status_code == 200 # redirect to calories breakdown


def test_super_access(client):
    create_account_super(client)
    response = client.get('/add', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/database', follow_redirects=True)
    assert response.status_code == 200
    assert b'Edit' in response.data

    response = client.get('/reportpage', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/reportgen', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/teambreakdown', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/breakdown', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/sleep', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/recovery', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/calories', follow_redirects=True)
    assert response.status_code == 200

    # response = client.get('/calendar', follow_redirects=True)
    # assert response.status_code == 200

    response = client.get('/edit/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'first_name' in response.data


def test_peak_access(client):
    create_account_peak(client)

    response = client.get('/teambreakdown', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/breakdown', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/sleep', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/recovery', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/calories', follow_redirects=True)
    assert response.status_code == 200


def test_coach_access(client):
    create_account_coach(client)
    response = client.get('/coach-dashboard', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/breakdown', follow_redirects=True)
    assert response.status_code == 200

    response = client.get('/sleep', follow_redirects=True)
    assert response.status_code == 200 # redirect to sleep breakdown

    response = client.get('/recovery', follow_redirects=True)
    assert response.status_code == 200 # redirect to recovery breakdown

    response = client.get('/calories', follow_redirects=True)
    assert response.status_code == 200 # redirect to calories breakdown


GCAL_OAUTH_SCOPES = ['https://www.googleapis.com/auth/calendar']
GCAL_SECRETS_FILE = 'oauth_credentials.json'
REDIRECT_URI = 'http://localhost:5000/oauth2callback'


# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         with app.app_context():
#             assert current_app.config["ENV"] == "production"
#         yield client

def test_calendar(client):
    # response = views.gcal_authorize()
    response = client.get('/calendar', follow_redirects=True)
    assert response.status_code == 200

# def test_sleep_breakdown(client):

def test_create_event(client):
    create_account_super(client)
    # response = client.get('/create-event', follow_redirects=True)
    # assert response.status_code == 200
    # assert b'event-name' in response.data
    # assert b'event-description' in response.data
    # assert b'event-location' in response.data
    # assert b'event-start-date' in response.data
    # assert b'event-start-time' in response.data
    # assert b'event-end-date' in response.data

    with client:
        response = client.post('/create-event',
                                data={  "event-name": "testing",
                                        "event-description": "still testing",
                                        "event-location:": "Miller",
                                        "event-start-date": "2022-12-18",
                                        "event-start-time": "09:00",
                                        "event-end-date": "2022-12-19",
                                        "event-end-time": "09:00"})
        print(response.data)
        assert response.status_code == 400
        


