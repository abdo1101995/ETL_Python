# Import the function needed
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
# Create the engine
engine = create_engine("postgresql+psycopg2://postgres:boody995@localhost:5432/Northdb")

# Create the session
session = Session(engine)

# Initialize the base and set inheritance
Base =declarative_base()

