from sqlalchemy import Integer,Enum,Double,Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship, mapped_column

from main import db

class Record(db.Model):
    id = Column(Integer, primary_key=True)
    operation_id = mapped_column(ForeignKey('operation.id'))
    user_id = mapped_column(ForeignKey('user.id'))
    amount = Column(Integer)
    user_balance = Column(Integer)
    operation_response = Column(Integer)
    
    operation = relationship('Operation',back_populates='children')
    user = relationship('User',back_populates='children')