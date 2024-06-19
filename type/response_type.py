# Description: This file is used to create a response type
# Author: Sebastian Gámez Ariza


# Importing libraries
from pydantic import BaseModel
from typing import Optional, TypeVar

T = TypeVar('T')


# Create the response type class
class ResponseType(BaseModel):
    status: int
    message: str
    data: Optional[T] = None
