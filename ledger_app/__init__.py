from flask import (
    Flask, render_template, url_for, request
)
from flask_sqlalchemy import SQLAlchemy
import uuid

# init the db to use it later in the models
# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = uuid.uuid4().hex
    app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///db.sqlite"

    # db.init_app(app)

    # blueprint for auth routes in our app
    from .auth.auth_routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .finances.fin_routes import fin as fin_blueprint
    app.register_blueprint(fin_blueprint)

    return app
