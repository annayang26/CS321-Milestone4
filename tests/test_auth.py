from website import auth
import json
import pytest 
import test_views

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

def test_failed_signup1(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'firstname' in response.data
    assert b'lastname' in response.data
    assert b'password1' in response.data
    assert b'password2' in response.data

    with client:
        response = client.post("/sign-up", 
                                data={"email": "ya",
                                      "firstname": "Super",
                                      "lastname": "Admin",
                                      "password1": "1111111",
                                      "password2": "1111111"})

        assert response.status_code == 200 # stays in signup page
        assert b'Email must be greater than 3 characters.' in response.data

def test_failed_signup2(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'firstname' in response.data
    assert b'lastname' in response.data
    assert b'password1' in response.data
    assert b'password2' in response.data

    with client:
        response = client.post("/sign-up", 
                                data={"email": "superadmin@colby.edu",
                                      "firstname": "S",
                                      "lastname": "Admin",
                                      "password1": "1111111",
                                      "password2": "1111111"})

        assert response.status_code == 200 # stays in signup page
        assert b'First name must be greater than 1 character.' in response.data

def test_failed_signup3(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'firstname' in response.data
    assert b'lastname' in response.data
    assert b'password1' in response.data
    assert b'password2' in response.data

    with client:
        response = client.post("/sign-up", 
                                data={"email": "superadmin@colby.edu",
                                      "firstname": "Super",
                                      "lastname": "Admin",
                                      "password1": "111111",
                                      "password2": "111111"})

        assert response.status_code == 200 # stays in signup page
        assert b'Password must be at least 7 characters.' in response.data

def test_failed_signup4(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'firstname' in response.data
    assert b'lastname' in response.data
    assert b'password1' in response.data
    assert b'password2' in response.data

    with client:
        response = client.post("/sign-up", 
                                data={"email": "superadmin@colby.edu",
                                      "firstname": "Super",
                                      "lastname": "Admin",
                                      "password1": "1111111",
                                      "password2": "1111111"})

        response = client.post("/sign-up", 
                                data={"email": "superadmin@colby.edu",
                                      "firstname": "Super",
                                      "lastname": "Admin",
                                      "password1": "1111111",
                                      "password2": "1111111"})
        # print(response.data)
        assert response.status_code == 302 # redirect to home page
        assert b'Redirecting' in response.data

def test_failed_signup5(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'firstname' in response.data
    assert b'lastname' in response.data
    assert b'password1' in response.data
    assert b'password2' in response.data

    with client:
        response = client.post("/sign-up", 
                                data={"email": "superadmin@colby.edu",
                                      "firstname": "Super",
                                      "lastname": "Admin",
                                      "password1": "1111111",
                                      "password2": "2222222"})

        assert response.status_code == 200 # stays in signup page
        assert b'Passwords do not match' in response.data

def test_success_signup(client):
    response = client.get('/sign-up')
    assert response.status_code == 200
    assert b'email' in response.data
    assert b'firstname' in response.data
    assert b'lastname' in response.data
    assert b'password1' in response.data
    assert b'password2' in response.data

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
        assert b'dashboard' in response.data

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

def test_add_user_failed(client):
    client.post("/sign-up",
                data={"email": "coach@colby.edu",
                      "firstname": "Coach",
                      "lastname": "One",
                      "password1": "1111111",
                      "password2": "1111111"})

    test_views.create_account_super(client)

    response = client.get('/add')
    assert response.status_code == 200

    with client:
        response = client.post("/add",
                                data={"email":"coach@colby.edu",
                                      "first_name":"Coach",
                                      "last_name":"One",
                                      "role":"coach",
                                      "team":"Soccer"})
        assert response.status_code == 302

def test_add_user_success(client):
    response = client.get('/add')
    assert response.status_code == 302

    with client:
        response = client.post("/add",
                                data={"email":"admin@colby.edu",
                                      "first_name":"Admin",
                                      "last_name":"One",
                                      "role":"admin"})
        response = client.post("/add",
                                data={"email":"coach@colby.edu",
                                      "first_name":"Coach",
                                      "last_name":"One",
                                      "role":"coach",
                                      "team":"Football"})
        response = client.post("/add",
                                data={"email":"hehe@colby.edu",
                                      "first_name":"Hehe",
                                      "last_name":"One",
                                      "role":"athlete",
                                      "team":"Football"})
        assert response.status_code == 302

def test_edit(client):
    response = client.get('/database')
    assert response.status_code == 302

    with client:
        response = client.post("/add",
                        data={"email":"admin@colby.edu",
                                "first_name":"Admin",
                                "last_name":"One",
                                "role":"admin"})
        response = client.post("/add",
                        data={"email":"athlete@colby.edu",
                                "first_name":"Athlete",
                                "last_name":"One",
                                "role":"athlete",
                                "team":"Soccer"})
        response = client.post("/edit/1",
                        data={"email":"athlete@colby.edu",
                                "first_name":"Athlete",
                                "last_name":"One",
                                "role":"athlete",
                                "team":"Swimming"})
        assert response.status_code == 400
        
def test_upload(client):
    response = client.get('/upload')
    assert response.status_code == 200
