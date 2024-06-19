# Description: This file handles the database connection related with the user
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy.orm import Session
from sqlalchemy import Engine, Select

# Importing the engine
from database.connection_database import engine

# Importing models
from models.user_model import User

# Importing types
from type.response_type import ResponseType
from type.user_type import UserType, UserUpdateType


# Create the client user class
class UserService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: Engine = engine

    # Create the method to create the user
    def create_user(self, user: UserUpdateType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the session
            with Session(self.engine) as session:
                # Create the user
                user_created = User(name=user.name, email=user.email, password=user.password, role=user.role)
                # Add the user to the session
                session.add(user_created)
                # Commit the session
                session.commit()
            # Create the response
            response_type = ResponseType(status=201, message="User created")
        except Exception as e:
            # Raise an error
            raise f'Error creating user: {e}'
        # Return the response type
        return response_type

    # Create the method to get the user by email
    def get_user_by_email(self, user: UserUpdateType) -> ResponseType:
        # Create the response type
        response_type: ResponseType[UserType]
        # Create the select query
        stmt: Select = Select(User).where(User.email == user.email)
        # Try to create a session and get the user
        try:
            with Session(self.engine) as session:
                # Get the user
                user_db: User = session.scalar(stmt)
                # If the user is not found
                if user_db is None:
                    # Create the response
                    response_type = ResponseType(status=404, message="User not found")
                else:
                    # Create the success response
                    response_type = ResponseType(
                        status=200,
                        message="User found",
                        data={
                            "id_user": user_db.id_user,
                            "name": user_db.name,
                            "email": user_db.email,
                            "password": user_db.password,
                            "role": user_db.role
                        }
                    )
        except Exception as e:
            # Throw an error
            raise f'Error getting user: {e}'
        # Return the response type
        return response_type
