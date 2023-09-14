#!/usr/bin/env python3


"""
Person resource related views
for the API
"""

from api.v1.views import app_views
from flask import make_response, request, abort, jsonify

from api.v1.utils import create_user, user_exists
from api.v1.exceptions import UserExistsAlready

@app_views.route('', methods = ['GET','POST', 'DELETE', 'PUT'], strict_slashes=False)
def handle_request():
    """
    Handle the request
    """
    if request.method == "POST":
        details = request.get_json()
        user_name = details.get('name')

        try:
            message = create_user('itsfoss')
            return jsonify({"message": message}), 200
        except UserExistsAlready:
            return jsonify({"error": f"user {user_name} already exists"}), 409
    