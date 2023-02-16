from sqlalchemy import Integer,Enum,Double,Column, String
from main import db

from .status import Status

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)
    status = Column(Enum(Status))

    def __init__(self,username,password_hash,status: Status) -> None:
        self.username = username
        self.password_hash = password_hash
        self.status = status
        