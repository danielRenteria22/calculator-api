from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers.user_controller import UserController
from controllers.response_helper import responde

user_routes = Blueprint('user', __name__,)

@user_routes.route('/login',methods = ['POST'])
def login(): return UserController.login()

@user_routes.route('/create',methods = ['POST'])
def create_user(): return UserController.create_user()

@user_routes.route("/refreshToken", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token(): return UserController.refresh_token()
    