from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SECRET_KEY'] = "change this to be a more random key"
application.config['UPLOAD_FOLDER'] = 'app/static/profiles'
application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pxewwkkroamxtb:d6adf4b5cc373fef4358993f0898a938f04759882392cc6a39daf588c8ab9a4e@ec2-107-20-233-240.compute-1.amazonaws.com:5432/d204k8m4akiu0a"
db = SQLAlchemy(application)
Base = db.Model
session = db.session
