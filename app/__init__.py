from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
bootstrap = Bootstrap5()

from config import config

def create_app(config_name):
    app = Flask(__name__, template_folder='template')
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/')

    return app