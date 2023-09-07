#!/usr/bin/env python3

"""
Views related to students
"""
from flask import jsonify, abort, request
import datetime
from api.v1.views import api_view


@api_view.route('/status/', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
        GET /api/v1/status
    to determine the status of the API
    Return:
        status of the API
    """
    return jsonify({"status": "ok"})


@api_view.route("/student", methods=["GET"], strict_slashes=False)
def students() -> str:
    """
    Mock some students and send 'em over
    Returns:
        some student mock objects
    """
    slack_name = request.args.get("slack_name", "Ebenezer Akhonya")
    track = request.args.get("track", "backend")

    format = "%Y-%m-%dT%H:%M:%SZ"
    utctime = datetime.datetime.utcnow().strftime(format)
    today = datetime.date.today().strftime("%A")
    github_repo = "https://github.com/Itsfoss0/hgnx_internship"

    resp_data = {
        "slack_name": slack_name,
        "current_day": today,
        "utc_time": utctime,
        "track": track,
        "github_file_url": f"{github_repo}/0x0-rest_api",
        "github_repo": github_repo,
        "status_code": 200
    }
    return jsonify(resp_data)


@api_view.route("/today", methods=['GET'], strict_slashes=False)
def today():
    """
    GET /api/v1/today
    Returns:
        returns the current day
    """
    format = "%Y-%m-%dT%H:%M:%SZ"
    utctime = datetime.datetime.utcnow().strftime(format)
    today = datetime.date.today().strftime("%A")
    return jsonify({
        "day": today,
        "utc_time": utctime,
        "status_code": 200
    }), 200


@api_view.route("/forbiden", methods=["GET", "POST"], strict_slashes=False)
def forbiden_path():
    abort(403)
