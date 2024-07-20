# Description: This file is used to validate and modify the data that is going to be sent to the database
# Author: Sebastian Gámez Ariza

# Importing services
from services.analysis_service import AnalysisService

# Importing types
from type.response_type import ResponseType
from type.analysis_type import AnalysisUpdateType, AnalysisType


# Create the analysis controller class
class AnalysisController:

    # Create constructor
    def __init__(self) -> None:
        self.analysis_service: AnalysisService = AnalysisService()

    # Create the method to create the analysis
    def create_analysis(self, analysis: AnalysisUpdateType) -> ResponseType:
        # try to create the analysis
        try:
            # Create the analysis
            response = self.analysis_service.create_analysis(analysis)
        except Exception as e:
            # Print the error
            print(f'Error creating analysis: {e}')
            raise e
        # Return the response
        return response

    # Create the method to get the analysis by user id
    def get_analysis_by_user_id(self, user_id: str) -> ResponseType:
        # try to get the analysis
        try:
            # Get the analysis
            response = self.analysis_service.get_analysis_by_user_id(user_id)
        except Exception as e:
            # Print the error
            print(f'Error getting analysis: {e}')
            # Raise the error
            raise e
        # Return the response
        return response

    # Create the method to get the analysis by question id
    def get_analysis_by_question_id(self, question_id: str) -> ResponseType:
        # try to get the analysis
        try:
            # Get the analysis
            response = self.analysis_service.get_analysis_by_question_id(question_id)
        except Exception as e:
            # Print the error
            print(f'Error getting analysis: {e}')
            # Raise the error
            raise e
        # Return the response
        return response
