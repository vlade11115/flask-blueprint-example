import flask

from hard_page.views import hard_page
from simple_page.views import simple_page


def create_app():
    app = flask.Flask(__name__)
    app.register_blueprint(simple_page, url_prefix="/simple")
    app.register_blueprint(hard_page, url_prefix="/hard")
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
