from __future__ import annotations

from sqlalchemy import Integer,Enum,Double,Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship, mapped_column

from .operation import Operation
from .user import User
from main import db

class Record(db.Model):
    id = Column(Integer, primary_key=True)
    operation_id = mapped_column(ForeignKey('operation.id'))
    user_id = mapped_column(ForeignKey('user.id'))
    amount = Column(Integer)
    user_balance = Column(Integer)
    operation_response = Column(String)
    
    operation = relationship('Operation',back_populates='children')
    user = relationship('User',back_populates='children')

    def __init__(self,operation: Operation,user: User,operation_response: int, user_balance: int,amount: int = None) -> None:
        self.operation = operation
        self.user = user
        self.operation_response = operation_response
        self.user_balance = user_balance
        self.amount = amount if amount is not None else - operation.cost

    def get_last_user_record(user: User) -> Record:
        record = db.query(Record)\
            .filter(Record.user==user)\
            .order_by(-Record.id)\
            .first()

        return record
        