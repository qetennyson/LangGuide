from flask import Flask
from flask_bootstrap import Bootstrap
from flask_babel import Babel

app = Flask(__name__)

from app import routes

bootstrap = Bootstrap(app)

babel = Babel(app)
