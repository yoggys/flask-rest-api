
import argparse

from waitress import serve

from core import app
from routes.UserRoute import User, UserEntry


class Server():
    def __init__(self, args: argparse.Namespace):
        self.dev = args.dev
        self.host = args.host
        self.port = args.port     
        
        with app.app_context():
            app.db.create_all()
            app.api.add_resource(User, '/api/v1/users')
            app.api.add_resource(UserEntry, '/api/v1/users/<int:id>')

    def run(self):
        if self.dev:
            app.run(host=self.host, port=self.port, debug=True)
        else:
            serve(app, host=self.host, port=self.port)