#!/usr/bin/env python3

"""
Route module for the API
"""

from flask import Flask, jsonify, request

from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run()