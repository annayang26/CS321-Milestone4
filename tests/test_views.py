from website import create_app
import json
import pytest 

def create_account_super(client):
    client.post("/signup",
                data={"email": "superadmin@colby.edu",
                        "first_name": "Super",
                        "last_name": "Admin",
                        "password1": "1111111",
                        "password2": "1111111"})

    client.post("/login",
                data={"email": "superadmin@colby.edu",
                        "password": "1111111"})


def create_account_coach(client):
    client.post("/signup",
                data={"email": "coach@colby.edu",
                        "first_name": "Coach",
                        "last_name": "One",
                        "password1": "1111111",
                        "password2": "1111111"})

    client.post("/login",
                data={"email": "coach@colby.edu",
                        "password": "1111111"})


def create_account_athlete(client):
    client.post("/signup",
                data={"email": "athlete@colby.edu",
                        "first_name": "Athlete",
                        "last_name": "One",
                        "password1": "1111111",
                        "password2": "1111111"})

    client.post("/login",
                data={"email": "athlete@colby.edu",
                        "password": "1111111"})


def test_access(client):
    print(client.access)
