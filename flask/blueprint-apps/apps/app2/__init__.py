from flask import Blueprint
from .urls import urls

app2 = Blueprint("app2", __name__, url_prefix="/app2")

for url, view_func, methods in urls:
    app2.add_url_rule(url, view_func=view_func, methods=methods)