#!/usr/bin/env python3

"""
Route module for the API
"""

from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from api.v1.views import api_view

app = Flask(__name__)
CORS(app, resources={r"/api*": {"origins": "*"}})
app.register_blueprint(api_view)


@app.errorhandler(403)
def forbiden(error) -> str:
    """
    Handle 403 error
    """
    return jsonify({"error": "Forbidden request"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
