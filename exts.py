from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_restful import Api
from flask_mail import Mail
from flask_cache import Cache


db = SQLAlchemy()
swagger = Swagger()
api = Api()
mail = Mail()
cache = Cache()
