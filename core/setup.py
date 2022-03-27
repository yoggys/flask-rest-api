from routes.UserRoute import User, UserParent

def init(app):
    app.db.create_all()
    app.api.add_resource(User, '/api/v1/users/<int:id>')
    app.api.add_resource(UserParent, '/api/v1/users')