#!/usr/bin/env python3

"""
Swagger documentation for the API
"""


from flask_swagger_ui import get_swaggerui_blueprint

BASE_URL = '/api/v1/docs'
API_URL = 'swagger.yml'
docs_bp = get_swaggerui_blueprint(
    BASE_URL,
    API_URL,
    config={"app_name": __name__ }
)