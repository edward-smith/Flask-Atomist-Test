# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['flasktest_app']

flasktest_app = Blueprint('flasktest_app', __name__)


@flasktest_app.route('/')
def index():
    return "Hello World!"
