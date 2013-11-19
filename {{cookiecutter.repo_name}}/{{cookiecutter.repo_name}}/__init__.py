# -*- coding: utf-8 -*-

from flask import Flask
import {{cookiecutter.repo_name}}.models
from models import db
import {{cookiecutter.repo_name}}.views


def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder='templates', static_folder='static')
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    return app
