#!/usr/bin/env python3
from os import getenv
from dotenv import dotenv_values

config = dotenv_values()

DB_NAME = config['DB_NAME']
DB_USER = config['DB_USER']
DB_PASSWORD = config['DB_PASSWORD']
DB_HOST = config['DB_HOST']
DB_PORT = 3306



