from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SECRET_KEY'] = "change this to be a more random key"
application.config['UPLOAD_FOLDER'] = 'app/static/profiles'
application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://udznciuarbcurz:c7a02c666749bbdf711ee95ce6aa50aaa9fa82d0f396ade149bf910c024981f3@ec2-50-19-109-120.compute-1.amazonaws.com:5432/d5rtn4iqg7sdn9"
db = SQLAlchemy(application)
Base = db.Model
session = db.session
