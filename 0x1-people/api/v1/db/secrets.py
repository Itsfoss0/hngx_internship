#!/usr/bin/env python3
from os import getenv

DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST', "127.0.0.1")
DB_PORT = getenv('DB_PORT', 3306)
