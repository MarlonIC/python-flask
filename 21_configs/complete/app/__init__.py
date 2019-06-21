from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app.routes import *

DBURI = "sqlite:///" + os.path.abspath('./database.db')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DBURI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


