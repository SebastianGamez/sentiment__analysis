# Description: This file is used to create the analysis type
# Author: Sebastian Gámez Ariza

# Importing libraries
from pydantic import BaseModel
from type.question_type import QuestionUpdateType
from type.user_type import UserUpdateType


# Create the analysis type
class AnalysisType(BaseModel):
    id_analysis: int
    answer: str
    pos: float
    neg: float
    neu: float
    question_id: int
    user_id: int
    question: QuestionUpdateType
    user: UserUpdateType


# Create the analysis update type
class AnalysisUpdateType(BaseModel):
    id_analysis: int | None = None
    answer: str | None = None
    pos: float | None = None
    neg: float | None = None
    neu: float | None = None
    question_id: int | None = None
    user_id: int | None = None
    question: QuestionUpdateType | None = None
    user: UserUpdateType | None = None
