from __future__ import annotations
import enum

from sqlalchemy import Integer,Enum,Double,Column
from main import db

class OperationTypes(enum.Enum):
    ADDITION = 'ADDITION'
    SUBSTRACTION = 'SUBSTRACTION'
    MULTIPLICATION = 'MULTIPLICATION'
    DIVISION = 'DIVISION'
    SQUARE_ROOT = 'SQUARE_ROOT'
    RANDOM_STRING = 'RANDOM_STRING'
    ADD_CREDIT='ADD_CREDIT'

class Operation(db.Model):
    id = Column(Integer, primary_key=True)
    cost = Column(Integer)
    type = Column(Enum(OperationTypes))

    @staticmethod
    def get_by_type(type: OperationTypes) -> Operation:
        operation = db.session.query(Operation).filter(Operation.type==type).first()
        return operation



