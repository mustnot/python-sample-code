from flask import request, jsonify

from .models import User

def signup():
    user = User(**request.form)
    return jsonify(user.dict())