# Description: Main file of the project
# Author: Sebastián Gámez Ariza


# Import FastAPI libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database connection
from database.connection_database import engine
from database.test_database import test_database_connection
from database.create_all_tables_database import create_all_tables
from routes.v1.user_route import user_router
from routes.v1.question_route import question_router

# Create the app
app = FastAPI()

# Set cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Activate the routes
app.include_router(user_router)
app.include_router(question_router)


# Create a startup event that runs when the server starts
@app.on_event("startup")
def startup() -> None:
    # Test the database connection
    test_database_connection(engine)
    # Create the tables
    create_all_tables()
