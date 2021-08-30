from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
jwt = JWTManager()

migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.secret_key = b'tutosecretkey'
    app.debug = True
    cors = CORS(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "tuto-secret" 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rares:raresasd123@localhost:5432/tuto_db'

    db.init_app(app)
    jwt.init_app(app)

    # with app.app_context():
    #     db.drop_all(app)

   

    migrate.init_app(app,db)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/')


    return app



    