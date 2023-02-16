import enum

from sqlalchemy import Integer,Enum,Double,Column
from main import db

class OperationTypes(enum.Enum):
    ADDITION = "ADDITION"
    SUBSTRACTION = "SUBSTRACTION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SQUARE_ROOT = "SQUARE_ROOT"
    RANDOM_STRING = "RANDOM_STRING"

class Operation(db.Model):
    id = Column(Integer, primary_key=True)
    cost = Column(Integer)
    type = Column(Enum(OperationTypes))



