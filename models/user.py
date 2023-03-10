from __future__ import annotations

from __future__ import annotations
from typing import List

from sqlalchemy import Integer,Enum,Double,Column, String
from sqlalchemy.orm import relationship,Mapped
from main import db

from .status import Status
from .operation import Operation
from .record import Record
from .soft_delete import SoftDelteModel

class User(db.Model,SoftDelteModel):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)
    status = Column(Enum(Status))
    records = relationship("Record", back_populates="user")

    def __init__(self,username,password_hash,status: Status) -> None:
        self.username = username
        self.password_hash = password_hash
        self.status = status

    @staticmethod
    def get_by_id(id: int) -> User:
        user = db.session.query(User).filter(User.id==id).first()
        return user

    @staticmethod
    def get_by_username(username: str) -> User:
        user = db.session.query(User).filter(User.username==username).first()
        return user

    def has_enough_credit(self,operation: Operation) -> bool:
        from .record import Record
        last_record = Record.get_last_user_record(self)
        return last_record.user_balance >= operation.cost

    def balance(self) -> int:
        from .record import Record
        last_record = Record.get_last_user_record(self)
        return last_record.user_balance

        