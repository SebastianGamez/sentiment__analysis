# Description: This file is used to create the question type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel


# Create the question type
class QuestionType(BaseModel):
    id_question: int
    question: str
    date: str
    analyses: list


# Create the question update type
class QuestionUpdateType(BaseModel):
    id_question: int | None = None
    question: str | None = None
    date: str | None = None
    analyses: list | None = None
