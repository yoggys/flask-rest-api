from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
import logging

from os import getcwd, makedirs

path = getcwd()+"/data"
makedirs(path, exist_ok=True)

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    filename=f'{path}/server.log', 
    filemode='w',
)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}/data.db'
app.db = SQLAlchemy(app)
app.ma = Marshmallow(app)
app.api = Api(app)