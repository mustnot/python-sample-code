from flask import Blueprint
from .urls import urls

app1 = Blueprint("app1", __name__, url_prefix="/app1")

for url, view_func, methods in urls:
    app1.add_url_rule(url, view_func=view_func, methods=methods)