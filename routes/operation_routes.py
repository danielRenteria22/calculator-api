from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.operations_controller import OperationController

operation_routes = Blueprint('operation', __name__,)

@jwt_required()
@operation_routes.route('/execute',methods = ['POST'])
def execute(): return OperationController.perform_operation()
    