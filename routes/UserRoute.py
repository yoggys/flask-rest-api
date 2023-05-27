from datetime import datetime

from flask import jsonify, Response
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

from core import app
from models.UserModel import UserModel, schema, schemas


def user_parser(need=False):
    user_args = reqparse.RequestParser()
    user_args.add_argument("email", type=str, required=need, location=['values'])
    user_args.add_argument("username", type=str, required=need, location=['values'])
    user_args.add_argument("password", type=str, required=need, location=['values'])
    return user_args

class User(Resource):
    def post(self) -> Response:
        args = user_parser(True).parse_args()
        
        user = UserModel(
            email=args["email"], 
            username=args["username"], 
            password=args["password"],
            created_at=datetime.now(),
        )
        app.db.session.add(user)
        
        try:
            app.db.session.commit()
        except IntegrityError:
            return {"message": "User with same email or username already exists"}, 409

        return jsonify(data = schema.dump(user))

    def get(self) -> Response:
        args = user_parser(False).parse_args()
        
        filter_params = { key: value for (key, value) in args.items() if value }
        user = UserModel.query.filter_by(**filter_params).all()
        
        return jsonify(data = schemas.dump(user))
    
    def delete(self) -> Response:
        users = UserModel.query.all()
        for user in users:
            app.db.session.delete(user)
        app.db.session.commit()
        
        return jsonify(data = schemas.dump(users))
    
class UserEntry(Resource):
    def find(self, id: int) -> UserModel:
        return UserModel.query.get_or_404(id, description=f"User not found (id={id})")

    def get(self, id: int) -> Response:
        user = self.find(id)
        return jsonify(data = schema.dump(user))
    
    def put(self, id: int) -> Response:
        user = self.find(id)
        
        args = user_parser(True).parse_args()
        for key in args:
            setattr(user, key, args[key])

        try:
            app.db.session.commit()
        except IntegrityError:
            return {"message": "User with same email or username already exists"}, 409

        return jsonify(data = schema.dump(user))

    def patch(self, id: int) -> Response:
        user = self.find(id)

        args = user_parser(False).parse_args()
        for key in args:
            if args[key]:
                setattr(user, key, args[key])
        
        try:
            app.db.session.commit()
        except IntegrityError:
            return {"message": "User with same email or username already exists"}, 409
        
        return jsonify(data = schema.dump(user))

    def delete(self, id: int) -> Response:
        user = self.find(id)
        
        app.db.session.delete(user)
        app.db.session.commit()
        
        return jsonify(data = schema.dump(user))