# Description: This file handles the database connection related with the analyses
# Author: Sebastian Gámez Ariza

# Importing libraries
from sqlalchemy.orm import Session
from sqlalchemy import Engine, Select
from pysentimiento import create_analyzer

# Importing the engine
from database.connection_database import engine

# Importing models
from models.model_model import Analysis

# Importing types
from type.response_type import ResponseType
from type.analysis_type import AnalysisType, AnalysisUpdateType


# Create the analysis service class
class AnalysisService:

    # Create constructor
    def __init__(self) -> None:
        self.engine: Engine = engine
        self.analyzer: create_analyzer = create_analyzer(task="sentiment", lang="es")

    # Create the method to create the analysis
    def create_analysis(self, analysis: AnalysisUpdateType) -> ResponseType:
        # Create the response type
        response_type: ResponseType
        try:
            # Create the session
            with Session(self.engine) as session:
                # Create the analysis
                analyzer_result = self.analyzer.predict(analysis.answer).probas
                # Create the analysis
                analysis_db = Analysis(
                    answer=analysis.answer,
                    pos=analyzer_result["POS"],
                    neg=analyzer_result["NEG"],
                    neu=analyzer_result["NEU"],
                    question_id=analysis.question_id,
                    user_id=analysis.user_id,

                )
                # Add the analysis to the session
                session.add(analysis_db)
                # Commit the session
                session.commit()
            # Create the response
            response_type = ResponseType(status=201, message="Analysis created")
        except Exception as e:
            # Print the error
            print(f'Error creating analysis {e}')
            # Raise an error
            raise e
        # Return the response type
        return response_type

    # Create the method to get the analysis by user id
    def get_analysis_by_user_id(self, user_id: str) -> ResponseType:
        # Create the response type
        response_type: ResponseType[AnalysisType]
        # Try to create a session and get the analysis
        try:
            with Session(self.engine) as session:
                # Get the analysis
                analysis_db = session.query(Analysis).filter(Analysis.user_id == user_id).all()
                # If the analysis is not found
                if analysis_db is None:
                    # Create the response
                    response_type = ResponseType(status=404, message="Analysis not found")
                else:
                    print(analysis_db)
                    # Create the response
                    response_type = ResponseType(
                        status=200,
                        message="Analysis found",
                        data=[
                            {
                                "id_analysis": analysis.id_analysis,
                                "answer": analysis.answer,
                                "pos": analysis.pos,
                                "neg": analysis.neg,
                                "neu": analysis.neu,
                                "question_id": analysis.question_id,
                                "user_id": analysis.user_id
                            } for analysis in analysis_db
                        ]
                    )
        except Exception as e:
            # Print the error
            print(f'Error getting analysis {e}')
            # Raise an error
            raise e
        # Return the response type
        return response_type

    # Create the method to get the analysis by question id
    def get_analysis_by_question_id(self, question_id: str) -> ResponseType:
        # Create the response type
        response_type: ResponseType[AnalysisType]
        # Try to create a session and get the analysis
        try:
            with Session(self.engine) as session:
                # Get the analysis
                analysis_db = session.query(Analysis).filter(Analysis.question_id == question_id).all()
                # If the analysis is not found
                if analysis_db is None:
                    # Create the response
                    response_type = ResponseType(status=404, message="Analysis not found")
                else:
                    # Create the response
                    response_type = ResponseType(
                        status=200,
                        message="Analysis found",
                        data=[
                            {
                                "id_analysis": analysis.id_analysis,
                                "answer": analysis.answer,
                                "pos": analysis.pos,
                                "neg": analysis.neg,
                                "neu": analysis.neu,
                                "question_id": analysis.question_id,
                                "user_id": analysis.user_id
                            } for analysis in analysis_db
                        ]
                    )
        except Exception as e:
            # Print the error
            print(f'Error getting analysis {e}')
            # Raise an error
            raise e
        # Return the response type
        return response_type
