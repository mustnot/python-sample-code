from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from .app1 import app1
    from .app2 import app2

    app.register_blueprint(app1)
    app.register_blueprint(app2)

    return app