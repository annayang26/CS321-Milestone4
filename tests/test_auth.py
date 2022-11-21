from website import auth
import json
import pytest 

def test_failed_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'password' in response.data

    with client:
        response = client.post("/login",
                                data={"email": "athlete@gmail.com",
                                      "password": "1111111"})
        assert response.status_code == 200
        assert b'Email does not exist' in response.data

def test_signup(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'password' in response.data
    assert b'firstname' in response.data
    assert b'lastname' in response.data

    with client:
        response = client.post("/sign-up", 
                                data={"email": "superadmin@colby.edu",
                                      "firstname": "Super",
                                      "lastname": "Admin",
                                      "password1": "1111111",
                                      "password2": "1111111"})

        assert response.status_code == 302 # redirect to home page
        assert b'Redirecting' in response.data

def test_success_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'password' in response.data

    with client:
        response = client.post("/sign-up",
                                data={"email": "superadmin@colby.edu",
                                        "firstname": "Super",
                                        "lastname": "Admin",
                                        "password1": "1111111",
                                        "password2": "1111111"})
        response = client.post("/login",
                                data={"email": "superadmin@colby.edu",
                                      "password": "1111111"})
        assert response.status_code == 302
        # assert b'dashboard' in response.data

def test_logout(client):
    with client: 
        response = client.post("/signup",
                                data={"email": "superadmin@colby.edu",
                                        "firstname": "Super",
                                        "lastname": "Admin",
                                        "password1": "1111111",
                                        "password2": "1111111"})
        response = client.post("/login",
                                data={"email": "superadmin@colby.edu",
                                        "password": "1111111"})
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        assert b'login' in response.data

def test_add_user_success(client):
    response = client.get('/add')
    assert response.status_code == 302

    with client:
        response = client.post("/add",
                                data={"email":"athleteNew@colby.edu",
                                      "first_name":"Athlete",
                                      "last_name":"New",
                                      "role":"athlete"})
        assert response.status_code == 302
        assert b'add' in response.data

def test_edit(client):
        pass