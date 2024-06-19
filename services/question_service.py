# Description: This file handles the database connection related with the questions
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy.orm import Session
from sqlalchemy import Engine, Select

# Importing the engine
from database.connection_database import engine

# Importing models
from models.question_model import Question

# Importing types
from type.response_type import ResponseType
from type.question_type import QuestionType, QuestionUpdateType


# Create the question service class
class QuestionService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: Engine = engine

    # Create the method to create the question
    def create_question(self, question: QuestionUpdateType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the session
            with Session(self.engine) as session:
                # Create the question
                question_created = Question(question=question.question, date=question.date)
                # Add the question to the session
                session.add(question_created)
                # Commit the session
                session.commit()
            # Create the response
            response_type = ResponseType(status=201, message="Question created")
        except Exception as e:
            # Raise an error
            raise f'Error creating question: {e}'
        # Return the response type
        return response_type

    # Create the method to get the question by id
    def get_question_by_id(self, id_question: str) -> ResponseType:
        # Create the response type
        response_type: ResponseType[QuestionType]
        # Create the select query
        stmt: Select = Select(Question).where(Question.id_question == id_question)
        # Try to create a session and get the question
        try:
            with Session(self.engine) as session:
                # Get the question
                question_db: Question = session.scalar(stmt)
                # If the question is not found
                if question_db is None:
                    # Create the response
                    response_type = ResponseType(status=404, message="Question not found")
                else:
                    # Create the response
                    response_type = ResponseType(
                        status=200,
                        message="Question found",
                        data={
                            "id_question": question_db.id_question,
                            "question": question_db.question,
                            "date": question_db.date
                        }
                    )
        except Exception as e:
            # Raise an error
            raise f'Error getting question: {e}'
        # Return the response type
        return response_type

    # Create the method to get all the questions
    def get_all_questions(self) -> ResponseType:
        # Create the response type
        response_type: ResponseType[list[QuestionType]]
        # Try to create a session and get the question
        try:
            with Session(self.engine) as session:
                # Get the questions
                questions_db = session.query(Question).all()
                # If there are no questions
                if questions_db is None:
                    # Create the response
                    response_type = ResponseType(status=404, message="Questions not found")
                else:
                    print(questions_db)
                    # Create the response
                    response_type = ResponseType(
                        status=200,
                        message="Questions found",
                        data=[
                            {
                                "id_question": question.id_question,
                                "question": question.question,
                                "date": question.date
                            } for question in questions_db
                        ]
                    )
        except Exception as e:
            # Raise an error
            raise f'Error getting questions: {e}'
        # Return the response type
        return response_type
