from sqlalchemy import Column, DateTime, Integer, String

from core import app


class UserModel(app.db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True, nullable=False)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=app.db.func.now())
    updated_at = Column(DateTime, default=app.db.func.now(), onupdate=app.db.func.now())

class UserSchema(app.ma.Schema):
    class Meta:
        fields = ("id", "email", "username", "password", "created_at", "updated_at")

schemas = UserSchema(many=True)
schema = UserSchema()