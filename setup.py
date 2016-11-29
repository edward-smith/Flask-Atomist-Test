# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from Flask-Atomist-Test import __version__


setup(
    name="Flask-Atomist-Test",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["Flask-Atomist-Test", "Flask-Atomist-Test.flasktest"],
    platforms=["any"]
)
