import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    #Secret key for form security
    app.config['SECRET_KEY'] = 'my_secret_key'

    db_url = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app,db)
    
    from . import routes
    app.register_blueprint(routes.main_bp)
    return app