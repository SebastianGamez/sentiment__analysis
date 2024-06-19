# Description: This file contains the routes for the user.
# Author: Sebastián Gámez Ariza

# Import libraries
from fastapi import APIRouter, HTTPException

# Import controllers
from controllers.user_controller import UserController

# Import types
from type.response_type import ResponseType
from type.user_type import UserType, UserUpdateType

# Create the employee controller instance
user_controller: UserController = UserController()

# Create the employee router
user_router: APIRouter = APIRouter(
    prefix="/api/user",
    tags=["User"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to create the user
@user_router.post("/register")
async def create_user(user: UserUpdateType) -> ResponseType:
    # Create the user
    response = user_controller.create_user(user)
    # Return the response
    return response


# Create the route to log in the user
@user_router.post("/login")
async def login_user(user: UserUpdateType) -> ResponseType:
    # Log in the user
    response = user_controller.login_user(user)
    # Return the response
    return response
