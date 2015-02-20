from flask import Flask, render_template

from .extensions import (
    db,
    migrate,
    debug_toolbar,
)

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/{{cookiecutter.app_name}}.db"
DEBUG = True
SECRET_KEY = 'development-key'

app = Flask(__name__)
app.config.from_object(__name__)

db.init_app(app)
debug_toolbar.init_app(app)
migrate.init_app(app, db)

from . import models, views