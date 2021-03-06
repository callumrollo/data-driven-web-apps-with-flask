import flask

from infrastructure import cookie_auth, request_dict
from pypi_org.infrastructure.view_modifiers import response
from services import user_service

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################### INDEX #################################


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    user_id = cookie_auth.get_user_id_via_auth_cookie(flask.request)
    if user_id is None:
        return flask.redirect('/account/login')
    user = user_service.find_user_by_id(user_id)
    if not user:
        return flask.redirect('/account/login')
    return {
        'user': user,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),

    }


# ################### REGISTER #################################

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    r = flask.request
    name = r.form.get('name')
    email = r.form.get('email', '').lower().strip()
    password = r.form.get('password').strip()

    if not name or not email or not password:
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': 'some required fields are missing.',
            'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }
    # TODO: create a user
    user = user_service.create_user(name, email, password)
    if not user:
        return {
            'name': name,
            'email': email,
            'password': password,
            'error': 'email already associated with registered user',
                     'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }
    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ################### LOGIN #################################

@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    data = request_dict.create()
    email = data.email.lower().strip()
    password = data.password.strip()

    if not email or not password:
        return {
            'email': email,
            'password': password,
            'error': 'some required fields are missing.',
                     'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }
    # TODO: validate a user
    user = user_service.login_user(email, password)
    if not user:
        return {
            'email': email,
            'password': password,
            'error': 'The account does not ecist or password is incorrect',
                     'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }
    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ################### LOGOUT #################################

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    cookie_auth.logout(resp)
    return resp
