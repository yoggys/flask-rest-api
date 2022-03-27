from core import app
from sqlalchemy import Column, Integer, String, DateTime

class UserModel(app.db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True, nullable=False)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    created_at = Column(DateTime, nullable=False)

class UserSchema(app.ma.Schema):
    class Meta:
        fields = ("id", "email", "username", "password", "created_at")

schemas = UserSchema(many=True)
schema = UserSchema()