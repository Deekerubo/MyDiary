from flask_api import FlaskAPI
from instance.config import app_config

def create_app(config_name):
    app = FlaskAPI(__name__, intstance_relative_config=True)
    app.config.from_pyfile('config.py')

    from app.views import *

    return app