# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.user_service import UserService

# Importing types
from type.response_type import ResponseType
from type.user_type import UserUpdateType, UserType
from bcrypt import gensalt, hashpw, checkpw
from jwt import encode

# Importing env variables
from config.env_variables_config import JWT_PASSWORD


# Create the user controller class
class UserController:

    # Create constructor
    def __init__(self) -> None:
        self.user_service: UserService = UserService()

    # Create the method to create the user
    def register_user(self, user: UserUpdateType) -> ResponseType:
        # try to create the user
        try:
            # Check if the email is already in use
            user_db = self.user_service.get_user_by_email(user)
            # If the user is not found
            if user_db.data is None:
                # Create the salt to hash the password
                salt = gensalt()
                # Hash the password
                user.password = hashpw(user.password.encode('utf-8'), salt).decode('utf-8')
                # Create the user
                self.user_service.create_user(user)
                # Create the response
                response = ResponseType(status=201, message="User created")
            else:
                # Create the response
                response = ResponseType(status=409, message="Email already in use")
        except Exception as e:
            raise f'Error registering user: {e}'
        # Return the response
        return response

    # Create the method to log in the user
    def login_user(self, user: UserUpdateType) -> ResponseType:
        # Try to log in the user
        try:
            # Try to get the user by email
            user_db: ResponseType[UserType] = self.user_service.get_user_by_email(user)
            # If the user isn't found
            if user_db.data is None:
                response = ResponseType(status=404, message="User or password incorrect")
            else:
                # Hash the password
                if checkpw(user.password.encode('utf-8'), user_db.data['password'].encode('utf-8')):
                    # Get the user data
                    token_data = user_db.data
                    # Remove the password from the data
                    token_data.pop('password')
                    # Create the token
                    token = encode(token_data, JWT_PASSWORD, algorithm='HS256')
                    # Create the response
                    response = ResponseType(status=200, message="User logged in", data=token)
                else:
                    response = ResponseType(status=401, message="User or password incorrect")
        except Exception as e:
            raise f'Error logging in user: {e}'
        # Return the response
        return response
