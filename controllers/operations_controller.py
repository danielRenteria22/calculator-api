import math
import requests
import os
import random

from flask import request
from jsonschema import validate
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt, verify_jwt_in_request


from .response_helper import responde
from .utils import encodePassword,checkPassword
from main import db
from models.user import User
from models.operation import Operation, OperationTypes
from models.status import Status
from models.record import Record

class OperationController:
    @staticmethod
    def operation_schema():
        user_schema = {
            'type' : 'object',
            'properties' : {
                'operand_1': {
                    'type': 'number'
                },
                'operand_2': {
                    'type': 'number'
                },
                'operation_type': {
                    'type': 'string',
                    'enum': [operation.value for operation in OperationTypes]
                }
            },
            'required': ['operand_1','operation_type']
        }
        return user_schema

    @staticmethod
    def list_schema():
        list_records_schema = {
            'type' : 'object',
            'properties' : {
                'page': {
                    'type': 'integer'
                },
                'items_per_page': {
                    'type': 'integer'
                },
                'operation_type': {
                    'type': 'string',
                    'enum': [operation.value for operation in OperationTypes]
                },
                'oder_by': {
                    'type': 'string',
                    'enum': ['operation_type','amount']
                },
                'order': {
                    'type': 'string',
                    'enum': ['desc','asc']
                }
            },
            'required': ['page','items_per_page']
        }
        return list_records_schema

    
    @staticmethod
    def perform_operation():
        body = request.get_json(force=True)
        try:
            validate(instance=body,schema=OperationController.operation_schema())
        except Exception as e:
            return responde(400,True,e.message,None)
        verify_jwt_in_request()
        claims = get_jwt()['sub']
        user = User.get_by_id(claims['user_id'])
        operation_type = OperationTypes[body['operation_type']]
        operation = Operation.get_by_type(operation_type)

        if not user.has_enough_credit(operation):
            failed_record = Record(operation,user,None,user.balance(),0)
            db.session.add(failed_record)
            db.session.commit()
            return responde(403,True,'Not enough credit for operation',{})
            
        result = None
        operand_1 = float(body['operand_1'])
        operand_2 = float(body['operand_2']) if 'operand_2' in body else None
        try:
            if operation.type == OperationTypes.ADDITION:
                if operand_2 is None: raise Exception('Operand 2 must be provided')
                result = operand_1 + operand_2
            elif operation.type == OperationTypes.MULTIPLICATION:
                if operand_2 is None: raise Exception('Operand 2 must be provided')
                result = operand_1 * operand_2
            elif operation.type == OperationTypes.DIVISION:
                if operand_2 == 0: raise Exception('Dividend can not be equal to zero')
                if operand_2 is None: raise Exception('Operand 2 must be provided')
                result = operand_1 / operand_2
            elif operation.type == OperationTypes.SUBSTRACTION:
                if operand_2 is None: raise Exception('Operand 2 must be provided')
                result = operand_1 - operand_2
            elif operation.type == OperationTypes.SQUARE_ROOT:
                if operand_1 < 0: raise Exception('Can not get squared root of negative number')
                result = math.sqrt(operand_1)
            elif operation.type == OperationTypes.RANDOM_STRING:
                result = OperationController.get_random_string()

            new_record = Record(operation,user,str(result),user.balance() - operation.cost)
            db.session.add(new_record)
            db.session.commit()
            return responde(200,False,'Operation succeded',result)
        except Exception as e:
            failed_record = Record(operation,user,None,user.balance(),0)
            db.session.add(failed_record)
            db.session.commit()
            return responde(200,True,'Error in the operation',str(e))
        
    @staticmethod
    def delete_record(id):
        verify_jwt_in_request()
        claims = get_jwt()['sub']
        user = User.get_by_id(claims['user_id'])
        record = Record.query.get(id)
        if(record.user_id != user.id):
            return responde(401,'Not auhtorized',None)
        if not record:
            return responde(404,True,'Record not found',None)
        
        print(record.query_class)
        record.deleted = True
        db.session.commit()
        return responde(200,True,'Record was deleted',None)

    @staticmethod
    def get_records():
        body = request.get_json(force=True)
        try:
            validate(instance=body,schema=OperationController.list_schema())
        except Exception as e:
            return responde(400,True,e.message,None)
        verify_jwt_in_request()
        claims = get_jwt()['sub']
        user = User.get_by_id(claims['user_id'])
        
        query = Record.query.filter(Record.user_id==user.id)
        if 'operation_type' in body:
            operation_type = OperationTypes[body['operation_type']]
            operation = Operation.get_by_type(operation_type)
            query = query.filter(Record.operation_id==operation.id)
        
        if 'oder_by' in body and 'order' in body:
            if body['oder_by'] == 'operation_type':
                order = Record.operation_id
            elif body['oder_by'] == 'amount':
                order = Record.amount
            
            if body['order'] == 'asc':
                order = order.asc()
            elif body['order'] == 'desc':
                order = order.desc()

            query = query.order_by(order)

        try:
            page = query.paginate(page=int(body['page']), per_page=int(body['items_per_page']))
            total_records = page.total
            total_pages = page.pages
            data = {
                'records': [r.to_json() for r in page.items],
                'next_page': page.has_next,
                'total_records': total_records,
                'total_pages': total_pages
            }
            return responde(200,False,'Records fetched correctly',data)
        except Exception as e:
            print(str(e))
            return responde(500,True,'Aun unexpected error ocurred',None)




    @staticmethod
    def get_random_string():
        url = 'https://api.random.org/json-rpc/4/invoke'
        data = {
            'jsonrpc': '2.0',
            'method': 'generateStrings',
            'params': {
                'apiKey': os.environ.get('RANDOM_API_KEY'),
                'n': 1,
                'length': 10,
                'characters': 'abcdefghijklmnopqrstuvwxyz',
            },
            'id': random.randint(1000,9000)
        }

        response = requests.post(url,json=data)
        response_json = response.json()
        if 'error' in response_json:
            raise Exception('Error while getting random string')
        
        return response_json['result']['random']['data'][0]



        

    
    