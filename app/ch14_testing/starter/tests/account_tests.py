from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from tests.test_client import flask_app
import unittest.mock

def test_example():
    print("test example...")
    assert 1 + 2 == 3

def test_register_validation_when_valid():
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

def test_register_validation_for_existing_user():
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
