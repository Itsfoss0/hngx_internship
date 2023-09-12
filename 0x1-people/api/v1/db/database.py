#!/usr/bin/env node

from sqlalchemy import create_engine
from secrets import (
    DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_PORT, DB_USER
)
connect_args = {
    "host": DB_HOST,
    "port": DB_PORT
}
CONNECTION_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

engine = create_engine(CONNECTION_URL, connect_args=connect_args)

connection = engine.connect()
connection.execute('SELECT name, emai, phone from users')