#!/usr/bin/env python3

"""
app blueprint
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api")
from api.v1.views.index import *
from api.v1.views.person import *