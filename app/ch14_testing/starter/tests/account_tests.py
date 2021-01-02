from flask import Response

from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from tests.test_client import flask_app, client
import unittest.mock

def test_example():
    print("test example...")
    assert 1 + 2 == 3

def test_vm_register_validation_when_valid():
    # Arrange
    form_data = {
        'name': 'marcos',
        'email': 'foo@bar.com',
        'password': 'a'*6,
    }
    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # Act
    target = 'pypi_org.services.user_service.find_user_by_email'
    with unittest.mock.patch(target, return_value=None):
        vm.validate()

    # Assert
    assert vm.error is None

def test_vm_register_validation_for_existing_user():
    # Arrange
    form_data = {
        'name': 'marcos',
        'email': 'foo@bar.com',
        'password': 'a'*6,
    }
    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    # Act
    target = 'pypi_org.services.user_service.find_user_by_email'
    test_user = User(email=form_data.get('email'))
    with unittest.mock.patch(target, return_value=test_user):
        vm.validate()

    # Assert
    assert vm.error is not None
    assert 'already exists' in vm.error



def test_v_register_view_new_user():
    # Arrange
    from pypi_org.views.account_views import register_post
    form_data = {
        'name': 'marcos',
        'email': 'foo@bar.com',
        'password': 'a'*6,
    }

    target = 'pypi_org.services.user_service.find_user_by_email'
    with unittest.mock.patch(target, return_value=None):
        target = 'pypi_org.services.user_service.create_user'
        with unittest.mock.patch(target, return_value=User()):
            with flask_app.test_request_context(path='/account/register', data=form_data):
                # Act
                resp: Response = register_post()



    # Assert
    assert resp.location == '/account'


def test_int_account_home_no_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    with unittest.mock.patch(target, return_value=None):
        resp: Response = client.get('/account')

    assert resp.status_code == 302
    assert resp.location == 'http://localhost/account/login'

def test_int_account_home_with_login(client):
    test_user = User(name='marcos', email='foo@bar.com')
    target = 'pypi_org.services.user_service.find_user_by_id'
    with unittest.mock.patch(target, return_value=test_user):
        resp: Response = client.get('/account')

    assert resp.status_code == 200
    assert b'marcos' in resp.data
