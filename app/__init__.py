from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_babel import Babel


app = Flask(__name__, static_folder='/Users/Scales/PycharmProjects/pbp_guide/app/static')
app.config.from_object(Config)

from app import routes

bootstrap = Bootstrap(app)

babel = Babel(app)
