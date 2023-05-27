import logging
from os import getcwd, makedirs, path

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

data_path = path.join(getcwd(), "data")
if not path.exists(data_path):
    makedirs(data_path)

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    filename=path.join(data_path, 'server.log'),
    filemode='w',
) 

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{data_path}/data.db'

app.db = SQLAlchemy(app)
app.ma = Marshmallow(app)
app.api = Api(app)