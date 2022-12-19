import pytest
from website import create_app, create_database, create_test_app, drop_database

@pytest.fixture()
def app():
    app1 = create_app()
    create_database(app1)
    app = create_test_app()
    app.config.update({
        "TESTING": True,
    })
    app.config['SECRET_KEY'] = 'my-secret-key'
    app.app_context().push()
    # other setup can go here

    yield app

    # clean up / reset resources here
    drop_database(app)


@pytest.fixture()
def client(app):
    return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()