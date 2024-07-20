# Description: This file creates all the tables in the database.
# Author: Sebastian Gámez Ariza

# Import the base class
from models.model_model import Base

# Import the engine
from database.connection_database import engine


# Create the tables
def create_all_tables() -> None:
    # Create the tables
    try:
        # Create the tables
        Base.metadata.create_all(engine)
        # Print a message
        print(f'\n', 'TABLES CREATED SUCCESSFUL'.center(105, '-'), end='\n\n')
    except Exception as e:
        # Print a message
        print(f'\n', 'TABLES CREATED ERROR'.center(105, '-'), end='\n\n')
