from core import app
from core.setup import init

# in a development server
if __name__ == '__main__':
   init(app)
   app.run()

# in a production deployment
# from waitress import serve
    
# if __name__ == '__main__':
#    init(app)
#    serve(app, host="127.0.0.1", port=5000)