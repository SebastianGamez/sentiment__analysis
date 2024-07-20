# Description: This file is used to create the user type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


class UserType(BaseModel):
    id_user: int
    name: str
    email: str
    password: str
    role: str
    analyses: list


# Create the user update type
class UserUpdateType(BaseModel):
    id_user: int | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None
    role: str | None = None
    analyses: list | None = None
