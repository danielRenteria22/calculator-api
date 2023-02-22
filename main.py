import os
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from controllers.jwt_controller import JWTController
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABSE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
JWTController.configureJWT()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# All models from migration
from models.operation import Operation
from models.record import Record
from models.user import User

# Needed for DB migrations
migrate = Migrate(app, db)

# Routes
from routes.user_routes import user_routes
from routes.operation_routes import operation_routes

app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(operation_routes, url_prefix='/operation')


