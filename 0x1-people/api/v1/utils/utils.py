#!/usr/bin/env python3

"""
Utility functions
"""
from typing import Union
from api.v1.db import cursor_object, db_object, DB_NAME
from api.v1.exceptions import UserExistsAlready

def user_exists(name: str) -> bool:
    """
    Check if a user exists already
    """

    cursor_object.execute("SELECT COUNT(*) FROM people WHERE name=%s", (name,))
    result = cursor_object.fetchall()
    exists = int(next(iter(result[0].values())))

    return (exists == 1)

def create_user(user_name: str) -> dict:
    """
    Create a new person in the database
    """
    
    if not user_exists(user_name):
        cursor_object.execute("INSERT INTO people (name) VALUES (%s)", (user_name,))
        db_object.commit()
        return {"user": f"{user_name}"}

    raise UserExistsAlready
