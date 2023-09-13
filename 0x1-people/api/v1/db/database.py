#!/usr/bin/env node

from sqlalchemy import (create_engine, text)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from typing import Union

from api.v1.models.person import Person
from secrets import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER
)


CONNECTION_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

class DB:
    """
    DB Class
    """

    def __init__(self) -> None:
        """
        Instantiate a DB session
        """
        self._engine = create_engine(CONNECTION_URL, connect_args={
            "host": "localhost",
            "port": 3306
        }, echo=False)
        self._session = None

    @property
    def _session(self) -> Session:
        if self._session is None:
            DBSession = sessionmaker(bind=self._engine)
            self._session = DBSession()
            return self._session
        return self._session

    @_session.setter
    def _session(self, new_session: Session) -> Session:
        self._session = new_session

    
    def add_person(self, **person_details: dict) -> Union[Person, None]:
        """
        Add a new person to the session and commit for persistence
        Args:
            person_details (dict): A dictionary of a persons details
        Returns:
            return the new Person
        """
        if person:
            new_person = Person(**person_details)
            self._session.add(new_person)
            self._session.commit()
            return new_person
        return
        
    def find_person_by(self, **filters: dict) -> Person:
        """
        Find a person using filters
        Args:
            filters (dict): filter to use
        Returns:
            returns the first match (if there's one)
        Exceptions:
            raises InvalidRequestError (if no filters are passed)
            raises NoResultsFound (if no person exists with such filters)
        """
        if filters:
            person = self._session.query(Person).filter_by(**filters).first()
            if person:
                return person
            return NoResultFound
        return InvalidRequestError

    def update_person(self, p_id: int,  **new_details: dict) -> Union[Person, None]:
        """
        Update person's details
        Args:
            p_id (int): The person's ID
            new_details (dict): The person's new details
        Returns:
            returns the person with the new details updated
        Exceptions:
        """
        filter_options = {
            "id": p_id
        }
        try:
            new_person = self.find_person_by(**filter_options)
            for key, value in new_details.items():
                if hasattr(new_person, key):
                    setattr(new_person, key, value)
                raise ValueError(f'People are not allowed to have {key} yet')
            self._session.commit()
            return new_person
        except (InvalidRequestError, NoResultFound):
            return None


    def delete_person(self, p_id: int) -> None:
        """
        Delete a person from the database
        Permanently
        """
        try:
            person_to_delete = self.find_person_by(id=p_id)
            self._session.delete(person_to_delete)
            self._session.commit()
        except(InvalidRequestError, NoResultFound):
            raise InvalidRequestError
