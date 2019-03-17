from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SECRET_KEY'] = "change this to be a more random key"
application.config['UPLOAD_FOLDER'] = 'app/static/profiles'
application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zuhhronmafyzwe:7f46727df561c73a7e6d29d8ebb8b6efabf3e6cf70570d374fe5c4bde8450ac1@ec2-50-19-109-120.compute-1.amazonaws.com:5432/d1v4jugmdblkhh"
db = SQLAlchemy(application)
Base = db.Model
session = db.session
