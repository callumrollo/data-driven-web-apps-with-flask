import flask
from pypi_org.services import package_service as package_services
from pypi_org.infrastructure.view_modifiers import response


blueprint = flask.Blueprint('home',__name__,template_folder='templates')

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_services.get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}