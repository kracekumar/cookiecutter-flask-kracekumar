# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from {{cookiecutter.repo_name}} import app
from coaster.sqlalchemy import BaseMixin, BaseNameMixin, BaseScopedNameMixin, BaseScopedIdNameMixin, BaseScopedIdMixin

db = SQLAlchemy(app)
