#!/usr/bin/env python3


"""
Person resource related views
for the API
"""

from api.v1.views import app_views
from flask import make_response, request, abort, jsonify

from api.v1.exceptions import UserExistsAlready, NoResultsFound, InvalidOperation
from api.v1.utils import (
    create_user,
    get_user_by_id,
    get_user_by_name,
    delete_user_name,
    delete_user_id,
    update_user,
    all_users
)


@app_views.route('', methods = ['GET','POST'], strict_slashes=False)
def handle_request():
    """
    Handle the request
    """
    if request.method == "POST":
        details = request.get_json()
        user_name = details.get('name')

        try:
            message = create_user(user_name)
            return jsonify({"message": message}), 200
        except UserExistsAlready:
            return jsonify({"error": f"user {user_name} already exists"}), 409
    elif request.method == "GET":
        users = all_users()
        return jsonify({"users": users})


@app_views.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def get_user(user_id: int) -> str:
    """
    /api/:user_id
    Returns the user based on the ID
    Args:
        user_id (int): User's ID
    """
    if request.method == "GET":
        try:
            user = get_user_by_id(user_id)
            return jsonify(user), 200
        except NoResultsFound:
            return jsonify({"error": f"User with id {user_id} doesn't exists"}), 404
    elif request.method == "DELETE":
        try:
            message = delete_user_id(user_id)
            return jsonify({"message": message}), 200
        except NoResultsFound:
            return jsonify({"error": f"User  with ID {user_id} not found"}), 404
    elif request.method == "PUT":
        try:
            new_name = request.get_json().get('name', 'Smith')
            message = update_user(user_id, new_name)
            return jsonify({"message": message }), 200
        except (InvalidOperation, NoResultsFound):
            return jsonify({"error": "Not updated. Try again latter"}), 400


@app_views.route('/<string:name>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def get_user_name(name: str) -> str:
    """
    /api/:user_name
    Returns the user based on the ID
    Args:
        user_id (int): User's ID
    """
    if request.method == "GET":
        try:
            user = get_user_by_name(name)
            return jsonify(user), 200
        except NoResultsFound:
            return jsonify({"error": f"User with name {name} doesn't exists"}), 404
    elif request.method == "DELETE":
        try:
            message = delete_user_name(name)
            return jsonify({"message": message}), 200
        except NoResultsFound:
            return jsonify({"error": f"User {name} not found"}), 404
    elif request.method == "PUT":
        try:
            new_name = request.get_json().get('name', 'Smith')
            message = update_user(name, new_name)
            return jsonify({"message": message }), 200
        except (InvalidOperation, NoResultsFound):
            return jsonify({"error": "Not updated. Try again latter"}), 400
