#!/usr/bin/env python3

"""
Utility functions
"""
from typing import Union
from api.v1.db import cursor_object, db_object, DB_NAME
from api.v1.exceptions import UserExistsAlready, InvalidOperation, NoResultsFound

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


def get_user_by_id(user_id: int) -> dict:
    """
    Get user object
    """
    cursor_object.execute("SELECT id, name FROM people where id = %s", (user_id,))
    results = cursor_object.fetchall()
    if bool(results) is False:
        raise NoResultsFound
    return results[0]

def get_user_by_name(user_name: str) -> dict:
    """
    Get user object
    """
    cursor_object.execute("SELECT id, name FROM people where name = %s", (user_name,))
    results = cursor_object.fetchall()
    if bool(results) is False:
        raise NoResultsFound
    return results[0]

def delete_user_name(name: str) -> str:
    """
    Delete User object using the name
    """
    try:
        if user_exists(name):
            cursor_object.execute("DELETE FROM people where name = %s", (name, ))
            db_object.commit()
            return f"user {name} Deleted"
        raise NoResultsFound
    except Exception:
        raise NoResultsFound

def delete_user_id(id: int) -> str:
    """
    Delete user object using ID
    """
    try:
        exists = get_user_by_id(id)
        cursor_object.execute('DELETE FROM people where id = %s', (id, ))
        db_object.commit()
        return f"user id {id} Deleted"
    except NoResultsFound:
        raise NoResultsFound
