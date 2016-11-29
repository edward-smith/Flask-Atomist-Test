# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, jsonify

from Flask-Atomist-Test.swagger import spec

__version__ = '0.1.0'
__all__ = ['create_app']


def create_app():
    """
    Create the :class:`flask.app.Flask` app, as well as its models.
    Also, register blueprints.
    """
    app = Flask(__name__)

    from Flask-Atomist-Test.views import main_app
    app.register_blueprint(main_app)

    from Flask-Atomist-Test.flasktest.views import flasktest_app
    app.register_blueprint(flasktest_app)

    return app

