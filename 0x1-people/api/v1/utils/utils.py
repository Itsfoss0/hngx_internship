#!/usr/bin/env python3

"""
Utility functions
"""
from typing import Union
from api.v1.db import cursor_object, db_object, DB_NAME
from api.v1.exceptions import UserExistsAlready, InvalidOperation, NoResultsFound

def all_users():
    """
    list all the users
    """
    cursor_object.execute("SELECT name, id FROM people")
    return list(cursor_object.fetchall())

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


def update_user(id_or_name: Union[int, str], new_name: str) -> str:
    """
    Update user details by ID or name.
    """
    try:
        if isinstance(id_or_name, int):
            exists = get_user_by_id(id_or_name)
            cursor_object.execute('UPDATE people SET name = %s WHERE id = %s', (new_name, id_or_name))
        elif isinstance(id_or_name, str):
            if user_exists(id_or_name):
                cursor_object.execute('UPDATE people SET name = %s WHERE name = %s', (new_name, id_or_name))
            raise NoResultsFound
        else:
            raise InvalidOperation("Invalid input type")
        db_object.commit()
        return f"User updated to {new_name}"
    except NoResultsFound:
        raise NoResultsFound
    except Exception:
        raise InvalidOperation("Failed to update user")
