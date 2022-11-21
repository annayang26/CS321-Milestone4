from website import create_app
import json
import pytest 

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
