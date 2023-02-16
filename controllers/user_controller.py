from flask import request
from jsonschema import validate
from flask_jwt_extended import create_access_token, create_refresh_token

from .response_helper import responde
from .utils import encodePassword,checkPassword
from main import db

class UserController:
    @staticmethod
    def user_schema():
        user_schema = {
            'type' : 'object',
            'properties' : {
                'username': {
                    'type': 'email'
                },
                'password': {
                    'type': 'string'
                }
            },
            'required': ['username','password']
        }
        return user_schema

    @staticmethod
    def login_schema():
        user_schema = {
            'type' : 'object',
            'properties' : {
                'username': {
                    'type': 'email'
                },
                'password': {
                    'type': 'string'
                }
            },
            'required': ['username','password']
        }
        return user_schema
        
    @staticmethod
    def create_user():
        from models.user import User
        from models.operation import Operation
        from models.status import Status

        body = request.get_json(force=True)
        try:
            validate(instance=body,schema=UserController.user_schema())
        except Exception as e:
            return responde(400,True,e.message,None)

        new_user = User(body['username'],encodePassword(body['password_hash']),Status.ACTIVE)
        try:
            db.session.add(new_user)
            db.session.commit()
            return responde(200,False,'User was created successfully',None)
        except:
            return responde(500,True,'An unexpected error ocurred',None)

    @staticmethod
    def login():
        body = request.get_json(force=True)
        try:
            validate(instance=body,schema=UserController.login_schema())
        except Exception as e:
            return responde(400,True,e.message,None)

        from models.user import User
        user = db.session.query(User).filter(User.username==body['username']).first()
        if not user: return responde(401,True,'Invalid credentials',None)
        if not checkPassword(body['password'],user.password_hash):
            return responde(401,True,'Invalid credentials',None)
        data = {
            'access_token': create_access_token(user.id),
            'refresh_token': create_refresh_token(user.id)
        }
        return responde(200,False,'Successful login',{'access_token': data})
        

        

        
        

