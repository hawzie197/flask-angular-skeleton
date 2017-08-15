from flask import Flask
from config import config

from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	# Register our blueprints
	from .default import default as default_blueprint
	app.register_blueprint(default_blueprint)

	# Initialize any extensions we are using
	bootstrap.init_app(app)
	db.init_app(app)

	return app