#!/usr/bin/env python3

"""
Index views
"""

from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status() -> str:
    """
        GET /api/status
        to check the status of the API
    """
    return jsonify({
        "status": "OK"
    })