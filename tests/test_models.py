from website.models import User

"""
This file (test_models.py) contains the unit tests for the models.py file.
"""


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password, and active fields are defined correctly
    """
    user = User('superadmin@colby.edu', '1111111', 'Super', 'Admin', 3, None, None)
    
    assert user.email == 'superadmin@colby.edu'
    assert user.password == '1111111'

    assert user.active != False
    assert user.first_name == 'Super'
    assert user.last_name == 'Admin'

    assert user.__repr__() == '<User Super>'
    assert user.is_authenticated
    assert user.is_active