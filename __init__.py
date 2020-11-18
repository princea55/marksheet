from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd4572ec42de00fc4c7648520db16fe0f'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://newuser:password@localhost/school"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
from marksheet import route