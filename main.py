# Description: Main file of the project
# Author: Sebastián Gámez Ariza


# Import FastAPI libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database connection
from database.connection_database import engine
from database.test_database import test_database_connection


# Test the database connection
test_database_connection(engine)

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
