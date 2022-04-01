
import argparse
from core import app
from routes.UserRoute import User, UserParent
from waitress import serve
class Server():
    def __init__(self):
        self.parse_args()
        app.db.create_all()
        app.api.add_resource(User, '/api/v1/users/<int:id>')
        app.api.add_resource(UserParent, '/api/v1/users')

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", default="127.0.0.1", type=str, help="Host name")
        parser.add_argument("--port", default=5000, type=int, help="Port number")
        parser.add_argument("--dev", action='store_true', help="Run server in development mode")
        self.args = parser.parse_args()

    def run(self):
        if self.args.dev:
            app.run(host=self.args.host, port=self.args.port, debug=True)
        else:
            serve(app, host=self.args.host, port=self.args.port)