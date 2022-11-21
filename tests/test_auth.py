from website import create_app
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
        assert b'User does not exist' in response.data

def test_signup(client):
    response = client.get('/signup')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'password' in response.data

    with client:
        response = client.post("/signup", 
                                data={"email": "superadmin@colby.edu",
                                        "first_name": "Super",
                                        "last_name": "Admin",
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
        response = client.post("/signup",
                                data={"email": "superadmin@colby.edu",
                                        "first_name": "Super",
                                        "last_name": "Admin",
                                        "password1": "1111111",
                                        "password2": "1111111"})
        response = client.post("/login",
                                data={"email": "superadmin@colby.edu",
                                        "password": "1111111"})
        print("\n\n", response.data)
        assert response.status_code == 302
        assert b'Redirecting' in response.data

def test_logout(client):
    with client: 
        response = client.post("/signup",
                                data={"email": "superadmin@colby.edu",
                                        "first_name": "Super",
                                        "last_name": "Admin",
                                        "password1": "1111111",
                                        "password2": "1111111"})
        response = client.post("/login",
                                data={"email": "superadmin@colby.edu",
                                        "password": "1111111"})
        response = client.get("/logout", follow_redirects=True)
        print("\n\n", response.data)
        assert response.status_code == 200
        assert b'login' in response.data