# Description: This file contains the routes for the analysis.
# Author: Sebastián Gámez Ariza

# Import libraries
from fastapi import APIRouter

# Import controllers
from controllers.analysis_controller import AnalysisController

# Import types
from type.response_type import ResponseType
from type.analysis_type import AnalysisUpdateType


# Create the analysis controller instance
analysis_controller: AnalysisController = AnalysisController()

# Create the analysis router
analysis_router: APIRouter = APIRouter(
    prefix="/api/analysis",
    tags=["Analysis"],
    responses={
        404: {"description": "Not found"}
    },
)


# Create the route to create the analysis
@analysis_router.post("/create")
async def create_analysis(analysis: AnalysisUpdateType) -> ResponseType:
    # Create the analysis
    response = analysis_controller.create_analysis(analysis)
    # Return the response
    return response


# Create the route to get the analysis by user id
@analysis_router.get("/user/{user_id}")
async def get_analysis_by_user_id(user_id: str) -> ResponseType:
    # Get the analysis
    response = analysis_controller.get_analysis_by_user_id(user_id)
    # Return the response
    return response


# Create the route to get the analysis by question id
@analysis_router.get("/question/{question_id}")
async def get_analysis_by_question_id(question_id: str) -> ResponseType:
    # Get the analysis
    response = analysis_controller.get_analysis_by_question_id(question_id)
    # Return the response
    return response


# Create the route to get the analysis statistics by user id
@analysis_router.get("/user/statistics/{user_id}")
async def get_analysis_statistics_by_user_id(user_id: str) -> ResponseType:
    # Get the analysis
    response = analysis_controller.get_analysis_statistics_by_user_id(user_id)
    # Return the response
    return response


# Create the route to get the analysis statistics by question id
@analysis_router.get("/question/statistics/{question_id}")
async def get_analysis_statistics_by_question_id(question_id: str) -> ResponseType:
    # Get the analysis
    response = analysis_controller.get_analysis_statistics_by_question_id(question_id)
    # Return the response
    return response
