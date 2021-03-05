from flask import Flask

from .urls import urls

def create_app() -> Flask:
    app = Flask(__name__)

    for url, view_func, methods in urls:
        app.add_url_rule(url, view_func=view_func, methods=methods)

    return app
