import enum

from sqlalchemy import Integer,Enum,Double,Column
from flask_sqlalchemy import Model

class OperationTypes(enum.Enum):
    ADDITION = "ADDITION"
    SUBSTRACTION = "SUBSTRACTION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    SQUARE_ROOT = "SQUARE_ROOT"
    RANDOM_STRING = "RANDOM_STRING"

class Operation(Model):
    id = Column(Integer, primary_key=True)
    cost = Column(Integer,min=0)
    type = Column(Enum(OperationTypes))



