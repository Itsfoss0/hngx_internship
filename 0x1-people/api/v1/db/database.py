


#!/usr/bin/env python3

"""database and cursor objects module"""

from MySQLdb import connect, cursors
from os import getenv

from .secrets import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER
)

db_object = connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASSWORD,
    db=DB_NAME
)
cursor_object = db_object.cursor(cursorclass=cursors.DictCursor)