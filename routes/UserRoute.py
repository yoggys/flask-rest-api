from models.UserModel import UserModel, schema, schemas
from flask_restful import Resource, reqparse
from datetime import datetime
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from core import app

def user_parser(need=False):
    user_args = reqparse.RequestParser()
    user_args.add_argument("email", type=str, required=need)
    user_args.add_argument("username", type=str, required=need)
    user_args.add_argument("password", type=str, required=need)
    return user_args

class UserParent(Resource):
    def post(self):
        args = user_parser(True).parse_args()
        obj = UserModel(
            email=args["email"], 
            username=args["username"], 
            password=args["password"],
            created_at=datetime.now(),
        )
        app.db.session.add(obj)
        
        try:
            app.db.session.commit()
        except IntegrityError:
            return {"message": "User with same email or username already exists"}, 409

        return jsonify(data = schema.dump(obj))

    def get(self):
        args = user_parser(False).parse_args()
        filter_data = {key: value for (key, value) in args.items() if value}
        obj = UserModel.query.filter_by(**filter_data).all()
        
        return jsonify(data = schemas.dump(obj))
    
class User(Resource):
    def find(self, id):
        return UserModel.query.get_or_404(id, description=f"User not found (id={id})")

    def get(self, id):
        obj = self.find(id)
        return jsonify(data = schema.dump(obj))
    
    def put(self, id):
        args = user_parser(True).parse_args()
        obj = self.find(id)
        for key in args:
            setattr(obj, key, args[key])

        try:
            app.db.session.commit()
        except IntegrityError:
            return {"message": "User with same email or username already exists"}, 409

        return jsonify(data = schema.dump(obj))

    def delete(self, id):
        obj = self.find(id)
        app.db.session.delete(obj)
        app.db.session.commit()
        return jsonify(data = schema.dump(obj))

    def patch(self, id):
        args = user_parser(False).parse_args()
        obj = self.find(id)

        for key in args:
            if args[key]:
                setattr(obj, key, args[key])
        try:
            app.db.session.commit()
        except IntegrityError:
            return {"message": "User with same email or username already exists"}, 409
        
        return jsonify(data = schema.dump(obj))