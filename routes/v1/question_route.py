# Description: This file contains the routes for the question.
# Author: Sebastián Gámez Ariza

# Import libraries
from fastapi import APIRouter

# Import controllers
from controllers.question_controller import QuestionController

# Import types
from type.response_type import ResponseType
from type.question_type import QuestionType, QuestionUpdateType


# Create the question controller instance
question_controller: QuestionController = QuestionController()

# Create the question router
question_router: APIRouter = APIRouter(
    prefix="/api/question",
    tags=["Question"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to create the question
@question_router.post("/create")
async def create_question(question: QuestionUpdateType) -> ResponseType:
    # Create the question
    response = question_controller.create_question(question)
    # Return the response
    return response


# Create the route to get all the questions
@question_router.get("/all")
async def get_all_questions() -> ResponseType:
    # Get all the questions
    response = question_controller.get_all_questions()
    # Return the response
    return response


# Create the route to get the question by id
@question_router.get("/{id_question}")
async def get_question_by_id(id_question: str) -> ResponseType:
    # Get the question
    response = question_controller.get_question_by_id(id_question)
    # Return the response
    return response
