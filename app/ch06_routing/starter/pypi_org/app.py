import flask


app = flask.Flask(__name__)

def register_blueprints():
    from pypi_org.views import home_views
    app.register_blueprint(home_views.blueprint)
    from pypi_org.views import package_views
    app.register_blueprint(package_views.blueprint)

def main():
    register_blueprints()
    app.run(debug=True)

if __name__ == '__main__':
    main()
