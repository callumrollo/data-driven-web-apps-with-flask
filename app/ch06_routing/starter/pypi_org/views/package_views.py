import flask
from pypi_org.services import package_service as package_services
from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
#@response(template_file='packages/detail.html')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)
    # return flask.render_template('home/index.html', packages=test_packages)
