from flask_routes import flask_app
from flask_config import secret_key

if __name__ == '__main__':

    flask_app.secret_key = secret_key

    flask_app.debug = True
    flask_app.run()
