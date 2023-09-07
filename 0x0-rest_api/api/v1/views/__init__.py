#!/usr/bin/env python3

"""
Initializing the API views
"""

from flask import Blueprint

api_view = Blueprint('api_view', __name__, url_prefix="/api")

from api.v1.views.student import *  # noqa E402
