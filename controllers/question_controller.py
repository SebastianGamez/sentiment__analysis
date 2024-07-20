# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.question_service import QuestionService

# Importing types
from type.response_type import ResponseType
from type.question_type import QuestionUpdateType


# Create the question controller class
class QuestionController:

    # Create constructor
    def __init__(self) -> None:
        self.question_service: QuestionService = QuestionService()

    # Create the method to create the question
    def create_question(self, question: QuestionUpdateType) -> ResponseType:
        # try to create the question
        try:
            # Create the question
            response = self.question_service.create_question(question)
        except Exception as e:
            # Print the error
            print(f'Error creating question: {e}')
            raise e
        # Return the response
        return response

    # Create the method to get the question by id
    def get_question_by_id(self, id_question: str) -> ResponseType:
        # try to get the question
        try:
            # Get the question
            response = self.question_service.get_question_by_id(id_question)
        except Exception as e:
            # Print the error
            print(f'Error getting question: {e}')
            # Raise the error
            raise e
        # Return the response
        return response

    # Create the method to get all the questions
    def get_all_questions(self) -> ResponseType:
        # try to get all the questions
        try:
            # Get all the questions
            response = self.question_service.get_all_questions()
        except Exception as e:
            # Print the error
            print(f'Error getting questions: {e}')
            # Raise the error
            raise e
        # Return the response
        return response
